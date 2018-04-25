import PyTango
import sys
import serial

arduino = serial.Serial('/dev/ttyACM0', 9600)

class TaurusTest(PyTango.Device_4Impl):

    def __init__(self, cl, name):
        PyTango.Device_4Impl.__init__(self, cl, name)
        TaurusTest.init_device(self)

    def delete_device(self):
        print "[Device delete_device method] for device", self.get_name()

    def init_device(self):
        print "In ", self.get_name(), "::init_device()"
        self.set_state(PyTango.DevState.ON)
        self.get_device_properties(self.get_device_class())
        self._position = 0.0

    def always_executed_hook(self):
        print "In ", self.get_name(), "::always_excuted_hook()"

    def read_attr_hardware(self, data):
        print "In ", self.get_name(), "::read_attr_hardware()"

    def read_Position(self, attr):
        lectura = arduino.readline()
        attr.set_value(int(lectura))
        print(lectura)

    def write_Position(self, attr):
        self._position = attr.get_write_value()

    def create_device_cb(self, device_name):
        print "About to create device", device_name

    def CreateTaurusTestDevice(self, device_name):
        klass = self.get_device_class()
        klass.create_device(device_name, cb=self.create_device_cb)

    def DeleteTaurusTestDevice(self, device_name):
        klass = self.get_device_class()
        klass.delete_device(device_name)


class TaurusTestClass(PyTango.DeviceClass):

    #    Class Properties
    class_property_list = {
    }

    #    Device Properties
    device_property_list = {
    }

    #    Command definitions
    cmd_list = {
        'CreateTaurusTestDevice':
            [[PyTango.DevString, 'device name'],
             [PyTango.DevVoid, ""]],
        'DeleteTaurusTestDevice':
            [[PyTango.DevString, 'device name'],
             [PyTango.DevVoid, ""]],
    }

    #    Attribute definitions
    attr_list = {
        'Position':
            [[PyTango.DevDouble,
              PyTango.SCALAR,
              PyTango.READ_WRITE],
             {
                'label': "Posicion",
                'unit': "cm",
                'format': "%8.3f",
                'max value': 100,
                'min value': 0,
                'max alarm': 90,
                'min alarm': 10,
                'max warning': 80,
                'min warning': 20,
            }],

    }

    def __init__(self, name):
        PyTango.DeviceClass.__init__(self, name)
        self.set_type(name)
        print "In TaurusTestClass  constructor"


if __name__ == '__main__':
    try:
        py = PyTango.Util(sys.argv)
        py.add_TgClass(TaurusTestClass, TaurusTest, 'TaurusTest')

        U = PyTango.Util.instance()
        U.server_init()
        U.server_run()

    except PyTango.DevFailed, e:
        print '-------> Received a DevFailed exception:', e
    except Exception, e:
        print '-------> An unforeseen exception occured....', e
