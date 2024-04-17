import noise
import numpy as np
import matplotlib.pyplot as plt

# Dimensioni del rumore
figure = (200, 200)

# Fattore di scala
dimension = 100.0

# Generazione della griglia di coordinate
def generate_perlin_noise(figure, dimension):
    world = np.zeros(figure)
    for i in range(figure[0]):
        for j in range(figure[1]):
            world[i][j] = noise.pnoise2(i/dimension, 
                                         j/dimension, 
                                         octaves=6, #le ottave servono ad indicare quanti livelli di rumore generare, in modo da aggiungere più dettagli 
                                         persistence=0.5, 
                                        #la persistenza indica quanto influiscono le ottave successive sul rumore generato
                                         lacunarity=2.0, 
                                        #indica la frequenza delle variazioni del rumore cambia ad ogni ottava. La lacunarità indica quanto più grande sarà la variazione del rumore.
                                         repeatx=1024, 
                                         repeaty=1024, 
                                         base=0)
    return world

# Generazione del rumore
world = generate_perlin_noise(figure, dimension)

# Visualizzazione del rumore generato
plt.imshow(world, cmap='gray', interpolation='nearest')
plt.colorbar()
plt.show()
