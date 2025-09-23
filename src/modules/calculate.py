import  pandas  as  pd
import  sympy   as  sp

###########################################################
###-------------------create_class----------------------###
###########################################################

class   relativity:
    
    def __init__(self, directory):
        self.directory  =   directory

        ###--------------------coordinates----------------------###
        input_coordinates   =   pd.read_csv(directory["input_coordinates"], header=None)
        input_coordinates   =   input_coordinates.values.tolist()  
        var =   [ item[0] for item in input_coordinates ]

        n   =   len(var)

        ###---------------------constants-----------------------###
        input_constants     =   pd.read_csv(directory["input_constants"], header=None)
        input_constants     =   input_constants.values.tolist()
        cte =   [ item[0] for item in input_constants ]

        ###-------------------metric_tensor---------------------###
        input_metric_tensor =   pd.read_csv(directory["input_metric_tensor"], header=None)
        input_metric_tensor =   input_metric_tensor.values.tolist()
        
        list_metric =   [ [ 0 for _ in range(n) ] for _ in range(n) ]
        itera   =   0
        for i   in  range(n):
            for j   in  range(n):
                if  i   <=  j:
                    list_metric[i][j]   =   input_metric_tensor[itera][0]
                    list_metric[j][i]   =   input_metric_tensor[itera][0]
                    itera   =   itera   +   1

        data_metric_tensor  =   pd.DataFrame(list_metric)
        self.metric_tensor  =   data_metric_tensor.to_csv(directory["metric_tensor"], index=False, header=None)
        
        ###---------------inverse_metric_tensor-----------------###
        data_inverse_metric =   pd.DataFrame(sp.Matrix(list_metric).inv().tolist())
        self.inverse_metric =   data_inverse_metric.to_csv(directory["inverse_metric"], index=False, header=None)




###########################################################
###-----------------texting_program---------------------###
###########################################################
import  os
os.system("clear")

dir =   {
    "input_metric_tensor":  "intro_data/tensor_metrico.dat",
    "input_coordinates":    "intro_data/variables.dat",
    "input_constants":      "intro_data/no_variables.dat",
    "metric_tensor":        "intro_data/metric_tensor.dat",
    "inverse_metric":       "intro_data/inverse_metric_tensor.dat",
}

g   =   relativity(dir)
g.metric_tensor
g.inverse_metric


