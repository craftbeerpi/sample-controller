from modules import cbpi
from modules.core.controller import KettleController
from modules.core.props import Property


@cbpi.controller
class SampleController(KettleController):

    # Custom Properties
    
    on = Property.Number("Offset On", True, 0)
    off = Property.Number("Offset Off", True, 0)

    def stop(self):
        '''
        Invoked when the automatic is stopped.
        Normally you switch off the actors and clean up everything
        :return: None
        '''
        super(KettleController, self).stop()
        self.heater_off()


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
            if self.get_temp() < self.get_target_temp() - int(self.on):
                # Switch the heater on. The value needs to be between 0 and 100. This is the power for PWM
                self.heater_on(100)
            elif self.get_temp() >= self.get_target_temp() - int(self.off):
                # switch heater off
                self.heater_off()
            else:
                self.heater_off()
            self.sleep(1)

