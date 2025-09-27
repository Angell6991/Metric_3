import  pandas  as  pd
import  sympy   as  sp

###########################################################
###-------------------create_class----------------------###
###########################################################

class   relativity:
    
    def __init__(self, data_input, data_save):
        self.data_input =   data_input
        self.data_save  =   data_save

        ###--------------------coordinates----------------------###
        input_coordinates   =   pd.read_csv(self.data_input[0], header=None)
        input_coordinates   =   input_coordinates.values.tolist()  
        self.var =   [ item[0] for item in input_coordinates ]

        self.n   =   len(self.var)

        ###---------------------constants-----------------------###
        input_constants     =   pd.read_csv(self.data_input[1], header=None)
        input_constants     =   input_constants.values.tolist()
        self.cte =   [ item[0] for item in input_constants ]

    ###########################################################
    ###-----------------save_coordinates--------------------###
    ###########################################################
    def save_coordinates(self):
        save    =   pd.DataFrame( { "arr": [self.var] } )
        return  save.to_pickle(self.data_save[0])

    ###########################################################
    ###------------------save_constants---------------------###
    ###########################################################
    def save_constants(self):
        save    =   pd.DataFrame( { "arr": [self.cte] } )
        return  save.to_pickle(self.data_save[1])

    ###########################################################
    ###-------------------metric_tensor---------------------###
    ###########################################################
    def metric_tensor(self):
        input_metric_tensor =   pd.read_csv(self.data_input[2], header=None)
        input_metric_tensor =   input_metric_tensor.values.tolist()

        list_metric =   [ [ 0 for _ in range(self.n) ] for _ in range(self.n) ]
        itera   =   0
        for i   in  range(self.n):
            for j   in  range(self.n):
                if  i   <=  j:
                    list_metric[i][j]   =   input_metric_tensor[itera][0]
                    list_metric[j][i]   =   input_metric_tensor[itera][0]
                    itera   =   itera   +   1

        save    =   pd.DataFrame( {"arr": [list_metric] } )
        return  save.to_pickle(self.data_save[2])
    
    ###########################################################
    ###---------------inverse_metric_tensor-----------------###
    ###########################################################
    def inverse_metric(self):
        metric =   pd.read_pickle(self.data_save[2])
        metric =   metric.loc[0, "arr"]
        inverse_metric =   sp.Matrix(metric).inv().tolist()
        save    =   pd.DataFrame( { "arr": [inverse_metric] } )
        return  save.to_pickle(self.data_save[3])

    ###########################################################
    ###---------------conexion_3_covariante-----------------###
    ###########################################################
    def christofell(self):
        G   =   pd.read_pickle(self.data_save[2])
        G   =   G.loc[0, "arr"]

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
                        list_interior[j][i]   =   sp.simplify( conexion(k, j, i) )
                        list_interior[i][j]   =   list_interior[j][i]
            
            list_exterior.append(list_interior)
            list_interior   =   []

        ###----------------save_data_in_.dat--------------------###
        save    =   pd.DataFrame( { "arr": [list_exterior] } )
        return  save.to_pickle(self.data_save[4])

    ###########################################################
    ###------------------Riemann_tensor---------------------###
    ###########################################################
    def riemann_tensor(self):

        ###--------------import_metric_inverse------------------###
        G_inv   =   pd.read_pickle(self.data_save[3])
        G_inv   =   G_inv.loc[0, "arr"]

        ###-----------------import_conexion---------------------###
        conexion    =   pd.read_pickle(self.data_save[4])
        conexion    =   conexion.loc[0, "arr"]

        ###----------------def_riemann_tensor-------------------###
        def R(p, i, j, k):
            return  (
                sp.diff(conexion[p][i][k], self.var[j]) -
                sp.diff(conexion[p][i][j], self.var[k]) +
                sum([ 
                    sum([ G_inv[q][m]*conexion[q][k][p]*conexion[m][i][j] for q in range(self.n) ]) 
                    for m in range(self.n) 
                ])   -
                sum([
                    sum([ G_inv[q][m]*conexion[q][j][p]*conexion[m][i][k] for q in range(self.n) ])
                    for m in range(self.n) 
                ])
            )

        ###------------calculate_full_riemann_tensor------------###
        list_exterior   =   [ [ 0 for _ in range(self.n) ] for _ in range(self.n) ]
        for p   in  range(self.n):
            for i   in  range(self.n):

                if  p   <   i:
                    list_interior   =   [ [ 0 for _ in range(self.n) ] for _ in range(self.n) ]
                    for j   in  range(self.n):
                        for k   in  range(self.n):
                            if  j   <  k:
                                list_interior[j][k] =   sp.simplify( R(p, i, j, k) )
                                list_interior[k][j] =   (-1)*list_interior[j][k]
                            elif    j   ==  k:
                                list_interior[j][k] =   0
                    
                    list_exterior[p][i] =   list_interior
                    list_exterior[i][p] =   -sp.Array(list_interior)

                elif    p   ==  i:
                    list_exterior[p][i] =   [[0]*self.n]*self.n

        ###----------------save_data_in_.dat--------------------###
        save    =   pd.DataFrame( { "arr": [list_exterior] } )
        return  save.to_pickle(self.data_save[5])
   
    ###########################################################
    ###--------------------Ricci_tensor---------------------###
    ###########################################################
    def ricci_tensor(self):

        ###--------------import_metric_inverse------------------###
        G_inv   =   pd.read_pickle(self.data_save[3])
        G_inv   =   G_inv.loc[0, "arr"]

        ###-----------------import_conexion---------------------###
        riemann    =   pd.read_pickle(self.data_save[5])
        riemann    =   riemann.loc[0, "arr"]
        
        ###-----------------def_ricci_tensor--------------------###
        def R(i, j):
            return  (
                sum([
                    sum([ G_inv[p][q]*riemann[p][i][q][j] for p in range(self.n) ]) 
                    for q in range(self.n)
                ])
            )

        ###-------------calculate_full_ricci_tensor-------------###
        list_ricci  =   [ [ 0 for _ in range(self.n) ] for _ in range(self.n) ]
        
        for i   in  range(self.n):
            for j   in  range(self.n):
                if  i   <=  j:
                    list_ricci[i][j]   =   sp.simplify( R(i, j) )
                    list_ricci[j][i]   =   list_ricci[i][j]
        
        ###----------------save_data_in_.dat--------------------###
        save    =   pd.DataFrame( { "arr": [list_ricci] } )
        return  save.to_pickle(self.data_save[6])
   
    ###########################################################
    ###------------------escalar_curvatura------------------###
    ###########################################################
    def e_curvatura(self):
        
        ###--------------import_metric_inverse------------------###
        G_inv   =   pd.read_pickle(self.data_save[3])
        G_inv   =   G_inv.loc[0, "arr"]

        ###---------------import_ricci_tensor-------------------###
        ricci    =   pd.read_pickle(self.data_save[6])
        ricci    =   ricci.loc[0, "arr"]
        
        ###---------------calculate_escalar_c-------------------###
        curvatura_e =  sum([ sum([ G_inv[q][p]*ricci[p][q] for q in range(self.n) ]) for p in range(self.n) ])

        ###----------------save_data_in_.dat--------------------###
        save    =   pd.DataFrame( { "arr": [curvatura_e] } )
        return  save.to_pickle(self.data_save[7])


###########################################################
###-----------------texting_program---------------------###
###########################################################
# import  os
# os.system("clear")

# ###---------------directory_data_input------------------###
# data_input  =   [
#     "intro_data/variables.dat",
#     "intro_data/no_variables.dat",
#     "intro_data/tensor_metrico.dat",
# ]

# ###---------------direrctory_data_save------------------###
# data_save   =   [
#     "intro_data/coordinates.dat",
#     "intro_data/constants.dat",
#     "intro_data/metric_tensor.dat",
#     "intro_data/inverse_metric_tensor.dat",
#     "intro_data/symbol_christofell.dat",
#     "intro_data/riemann_tensor.dat",
#     "intro_data/ricci_tensor.dat",
#     "intro_data/escalar_curvatura.dat",
# ]

# ###-----------------texting_functions-------------------###
# g   =   relativity(data_input, data_save)
# g.save_coordinates()
# g.save_constants()
# g.metric_tensor()
# g.inverse_metric()
# g.christofell()
# g.riemann_tensor()
# g.ricci_tensor()
# g.e_curvatura()


