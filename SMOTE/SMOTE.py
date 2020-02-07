import arcpy
import numpy as np
import sys
import datetime
from timeit import default_timer as timer
from imblearn.over_sampling import SMOTE 

# Global Name for the messages object and be called from any function
MESSAGES = None

# Verbosity switch, True to print more detailed information
VERBOSE = True
if VERBOSE:
    def _verbose_print(text):
        #global MESSAGES
        arcpy.AddMessage("Verbose: " + str(text))
else:
    _verbose_print = lambda *a: None

def _get_fields(feature_layer, fields_name):
    """
        _get_fields
            Gets all the values for the given fields and returns a numpy-array with the values 
        :param feature_layer: Name of the feature layer to extract the values
        :param fields_name: List with the name of the fields to extract features
        :return: 
    """
    _verbose_print("feature_layer: {}".format(feature_layer))
    _verbose_print("fields_name: {}".format(fields_name))

    # Since integers does not support NAN values, the method throws an error, then NAN values are assigned to the
    # maximum integer
    if type(fields_name) == list:
        fields_name = [str(x) for x in fields_name]
    else:
        fields_name = [str(fields_name)]

    fields = ["SHAPE@X","SHAPE@Y"] + fields_name
    #_verbose_print(fields)
    try:
        fi = arcpy.da.FeatureClassToNumPyArray(feature_layer, fields)
    except TypeError:
        _verbose_print("Failed importing with nans, possibly a integer feature class")
        fi = arcpy.da.FeatureClassToNumPyArray(feature_layer, fields, null_value=sys.maxint)

    # Cast to floating point numbers
    field = np.array([[elem * 1.0 for elem in row] for row in fi])

    # If only one field is given the matrix needs to be flatten to a vector
    if not isinstance(fields_name, list):
        field = field.flatten()
    # Assign NAN to the numbers with maximum integer value
    field[field == sys.maxsize] = np.NaN

    return field

train_points = arcpy.GetParameterAsText(0)
train_regressors_name = arcpy.GetParameterAsText(1).split(";")
train_response_name = arcpy.GetParameterAsText(2)
output_points = arcpy.GetParameterAsText(3)
smote_ratio = int(arcpy.GetParameterAsText(4))
smote_knn = int(arcpy.GetParameterAsText(5))
smote_kind = 'regular'

train_regressors = _get_fields(train_points, train_regressors_name)
train_response = _get_fields(train_points, train_response_name)
#arcpy.AddMessage(train_regressors)
#arcpy.AddMessage(train_response)
train_response = train_response[:,2]

original_len = len(train_response[np.where(train_response == 1)])
#arcpy.AddMessage(original_len)
smote_len = int(original_len*(smote_ratio/100))
#arcpy.AddMessage(smote_len)
negative_len = len(train_response[np.where(train_response == -1)])
#arcpy.AddMessage(negative_len)

#arcpy.AddMessage(train_regressors.shape)
#arcpy.AddMessage(train_response.shape)

sm = SMOTE(ratio={1: smote_len, -1: negative_len}, random_state=420, k_neighbors=smote_knn, m_neighbors=10, out_step=0.5, kind=smote_kind, svm_estimator=None, n_jobs=1)
X_res, y_res  = sm.fit_sample(train_regressors, train_response)
#arcpy.AddMessage(np.c_[X_res, y_res])
#arcpy.AddMessage(y_res)

arcpy.AddMessage("X length: {}".format(train_regressors.shape[0]))
arcpy.AddMessage("y length: {}".format(train_response.shape[0]))
arcpy.AddMessage("new X length: {}".format(X_res.shape[0]))
arcpy.AddMessage("new y_res length: {}".format(y_res.shape[0]))

out_fields = ['X','Y'] + [str(x) for x in train_regressors_name] + [str(train_response_name)]

out_fields_type = {'names': tuple(name for name in out_fields), 'formats': tuple('f8' for i in range(len(out_fields)))}
#arcpy.AddMessage(out_fields_type)

structured_output = np.core.records.fromarrays(np.c_[X_res, y_res].transpose(), 
                                             names=','.join(out_fields_type['names']),
                                             formats = ','.join(out_fields_type['formats']))
#arcpy.AddMessage(structured_output)

SR = arcpy.Describe(train_points).spatialReference
arcpy.da.NumPyArrayToFeatureClass(structured_output, output_points, ['X','Y'], SR)