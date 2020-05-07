from layer import Layer

class FirstLayer(Layer):
    def __init__(self,nrNeurons,bias=False):
        if bias:
            noNeurons += 1
        Layer.__init__(self,1,nrNeurons)

    def forward(self, inputs):
        for i in range(len(self.neurons)):
            self.neurons[i].activate([inputs[i]])
        return([x.output for x in self.neurons])
