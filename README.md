# Sample Code for Custom Controller

With a controller is possible to control the kettle temperature

```
from modules import cbpi
from modules.core.controller import KettleController
from modules.core.props import Property


@cbpi.controller
class SampleController(KettleController):

    # Custom Properties
    
    p1 = Property.Number("My Number Label", True, 0)
    text1 = Property.Text("My Label", True, "Hello World")

    def stop(self):
        '''
        Invoked when the automatic is stopped.
        Normally you switch off the actors and clean up everything
        :return: None
        '''
        super(KettleController, self).stop()
        pass


    def init(self):
        '''
        Invoked when the kettle automatic is switched on. 
        :return: 
        '''
        pass
    
    def run(self):
        '''
        Each controller is exectuted in its own thread. The run method is the entry point
        :return: 
        '''
        while self.is_running():
            # YOUR LOGIC GOES HERE
            
            # Access the proerties
            self.text1
            self.p1
            
            self.sleep(1)
```
