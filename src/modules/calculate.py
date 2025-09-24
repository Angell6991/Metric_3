import  pandas  as  pd
import  sympy   as  sp

###########################################################
###-------------------create_class----------------------###
###########################################################

class   relativity:
    
    def __init__(self, directory):
        self.directory  =   directory

        ###--------------------coordinates----------------------###
        input_coordinates   =   pd.read_csv(self.directory["input_coordinates"], header=None)
        input_coordinates   =   input_coordinates.values.tolist()  
        self.var =   [ item[0] for item in input_coordinates ]

        self.n   =   len(self.var)

        ###---------------------constants-----------------------###
        input_constants     =   pd.read_csv(self.directory["input_constants"], header=None)
        input_constants     =   input_constants.values.tolist()
        self.cte =   [ item[0] for item in input_constants ]


    ###########################################################
    ###-------------------metric_tensor---------------------###
    ###########################################################
    def metric_tensor(self):
        input_metric_tensor =   pd.read_csv(self.directory["input_metric_tensor"], header=None)
        input_metric_tensor =   input_metric_tensor.values.tolist()

        list_metric =   [ [ 0 for _ in range(self.n) ] for _ in range(self.n) ]
        itera   =   0
        for i   in  range(self.n):
            for j   in  range(self.n):
                if  i   <=  j:
                    list_metric[i][j]   =   input_metric_tensor[itera][0]
                    list_metric[j][i]   =   input_metric_tensor[itera][0]
                    itera   =   itera   +   1

        data_metric_tensor  =   pd.DataFrame(list_metric)
        return  data_metric_tensor.to_csv(self.directory["metric_tensor"], index=False, header=None)
    
    ###########################################################
    ###---------------inverse_metric_tensor-----------------###
    ###########################################################
    def inverse_metric(self):
        list_metric =   pd.read_csv(self.directory["metric_tensor"], header=None).values.tolist()
        data_inverse_metric =   pd.DataFrame(sp.Matrix(list_metric).inv().tolist())
        return  data_inverse_metric.to_csv(self.directory["inverse_metric"], index=False, header=None)

    ###########################################################
    ###---------------conexion_3_covariante-----------------###
    ###########################################################
    def christofell(self):
        G   =   pd.read_csv(self.directory["metric_tensor"], header=None).values.tolist()
        # G   =   sp.Matrix(G)

        ###-------------------def_conexion----------------------###
        def conexion(k, j, i):
            return   (
                sp.diff(G[j][k], self.var[i])   + 
                sp.diff(G[i][k], self.var[j])   - 
                sp.diff(G[i][j], self.var[k])    
            )/2
        
        ###--------------calculate_full_conexion----------------###
        list_exterior   =   []
        for k   in  range(self.n):
            list_interior   =   [ [ 0 for _ in range(self.n) ] for _ in range(self.n) ]
            
            for j   in  range(self.n):
                for i   in  range(self.n):
                    if  j   <=  i:
                        list_interior[j][i]   =   conexion(k, j, i)
                        list_interior[i][j]   =   list_interior[j][i]
            
            list_exterior.append(list_interior)
            list_interior   =   []

        ###----------------save_data_in_.dat--------------------###
        save    =   pd.DataFrame( { "arr": [list_exterior] } )
        return  save.to_pickle(self.directory["christofell"])

    ###########################################################
    ###------------------Riemann_tensor---------------------###
    ###########################################################
    def riemann_tensor(self):

        ###--------------import_metric_inverse------------------###
        G_inv   =   pd.read_csv(self.directory["inverse_metric"], header=None).values.tolist()

        ###-----------------import_conexion---------------------###
        conexion   =   pd.read_pickle(self.directory["christofell"])
        conexion   =   conexion.loc[0, "arr"]

        return  print(G_inv)
    


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
    "christofell":          "intro_data/symbol_christofell.dat",
    "riemann_tensor":       "intro_data/riemann_tensor.dat",
}

g   =   relativity(dir)
# g.metric_tensor()
# g.inverse_metric()
# g.christofell()
g.riemann_tensor()


