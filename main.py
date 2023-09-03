from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
class Brownian():
    """
    un constructeur du mouvement brownine
    """
    def __init__(self,x0=0):
        """
        classe d'initialisation
        """
        assert (type(x0)==float or type(x0)==int or x0 is None), "attend un float ou None dans les valeurs intiales"

        self.x0 = float(x0)
    def gen_normal(self,n_pas=100):
        """
        Genere un mouvement en dessinant a 
        partir de la distribution normale

        Arguments:
            n_pas: Nombre de pas

        Returns:
        un NumPy array avec `n_pas` points
        """
        if n_pas < 30:
            print("ATTENTION! le nombre de pas est tres faible, il peut pas donner une bonne sequence stochastique")

            w = np.ones(n_pas)*self.x0
            for i in range(1,n_pas):
        # echantillons de la repartition normale
                yi = np.random.normal()
        # procéde de Weiner
                w[i] = w[i-1]+(yi/np.sqrt(n_pas))
        return w
b1 = Brownian()
b2 = Brownian()
b3 = Brownian()
x = b1.gen_normal(1000)
y = b2.gen_normal(1000)
z = b3.gen_normal(1000)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(x, y, 
z,c=z,cmap='BuGn',linewidth=0.5)
import matplotlib.pylab as p ;
from mpl_toolkits . mplot3d import Axes3D ;
from numpy import * ;
print ( "Working ,waitforthefigurea f t e r 100i t e r a t i o n s" ) 
Nxmax = 70 ; Nymax=20; IL = 20; H = 10 ; T =10;h = 5.
u = p.zeros( (Nxmax+1 , Nymax+1) ,float ) # le flux
w = p.zeros( (Nxmax+1 , Nymax+1) ,float ) # Veracité
V0 = 1.0; omega = 0.1; nu = 1.; iter = 0; R=V0*h/nu
def limite ( ) :
    for i in range (0 , Nxmax+1) : # Initialisation du flux 
        for j in range (0 , Nymax+1) : # Initia du veracité
            w[ i ,j ] = 0.
            u [ i ,j ] = j* V0 
    for i in range (0 , Nxmax+1 ) : # surface du fluid
        u[i,Nymax] = u[i,19] + V0*h 
        w[ i , 19] = 0.
    for j in range (0 , Nymax+1) :
        u [1 ,j ] = u [0 ,j ] 
        w[0 ,j ] = 0. # le flx est rectiliqne
    for i in range (0 , Nxmax+1) : # les limites du debut
        if i <= IL and i >= IL+T:
            u [ i ,0] = 0.
            w[ i ,0] = 0.
    for j in range (1 , Nymax ) : # les limites à la fin
        w[Nxmax,j ] = w[Nxmax-1,j ] 
        u [Nxmax,j ] = u [Nxmax-1,j ] 
def plaque ( ) : # l’influence d’une plaque sur l flux
    for j in range(0 , H+1) : # les cotés
        w[ IL,j ] = -2*u[IL-1,j]/( h*h ) # l’avant 
        w[ IL+T,j ] = -2* u [ IL + T + 1 ,j ] / ( h*h ) # le derrier
    for i in range ( IL ,IL+T+1) : w[ i , H-1] =-2* u [ i , H] / (h*h ) ;
    for i in range ( IL ,IL+T+1) :
        for j in range (0 , H+1) :
            u [ IL ,j ] = 0. # l’avant
            u [ IL+T,j ] = 0. # dérriere
            u [ i , H] = 0 ; # au dessus
def relax( ) : # la relaxation du flux
    plaque( ) # la condition 
    for i in range (1 , Nxmax) : # le flux relaxé 
        for j in range(1 , Nymax ) :
            r1 = omega * ((u[i+1,j] + u[i-1,j] + u[i,j+1] + u[i,j-1]+(h*h)*w[i,j])/4-u[i,j]) 
            u [ i ,j ] += r1 
    for i in range (1 , Nxmax) : # relaxation du verocité
        for j in range (1 , Nymax ) :
            a1 = w[ i +1 ,j ] + w[ i-1, j ] + w[ i , j +1] + w[ i , j-1] 
            a2 = (u [ i , j +1]- u [ i , j-1]) *(w[ i +1 , j ]-w[ i-1 ,j ] ) 
            a3 = (u [ i +1 , j ]-u [ i-1, j ] ) *(w[ i , j +1]-w[ i ,j-1 ]) 
            r2 = omega *(( a1-(R / 4. ) *( a2-a3 )) / 4. - w[ i , j ] ) 
            w[ i ,j ] += r2 
    limite() 
    while( iter <= 100) :
        iter += 1 
        if iter%10 == 0 :print(iter) 
        relax () 
    for i in range(0 , Nxmax+1) :
        for j in range (0 , Nymax+ 1) : u[ i , j ] = u [ i , j ] / V0/h # V0h units
    x = range (0 , Nxmax-1) ; y = range (0 , Nymax-1) 
    X, Y = p.meshgrid ( x ,y )
def functz (u) : # Stream flow 
    z = u [X, Y] 
    return z 
Z= functz (w) 
fig = p.figure()
ax = Axes3D(fig)
ax . plot_wireframe ( X, Y, Z, color = 'r') 
ax.set_xlabel( 'X' ) 
ax.set_ylabel( 'Y' ) 
ax.set_zlabel( ' flux du gaz porteur ' ) 
p . show () 
