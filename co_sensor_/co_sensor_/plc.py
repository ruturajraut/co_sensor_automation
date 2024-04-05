import pyads
import time
import gvl  # Importing gvl.py

plc_in = ''
plc_out = ''

def check_controller_availability(parameter_list):
    global plc_in
    global plc_out
    """
    Function to check the availability of controllers based on the provided parameters.
    
    Args:
        parameter_list (dict): A dictionary containing parameters related to controllers.

    Returns:
        None
    """
    isControllerAvailable = False
    while isControllerAvailable == False:
        controllerNum = 0
        for controller_details in parameter_list.get("controllers", []):
            controller_name = controller_details.get("controller_name")
            controller_net_id = controller_details.get("controller_net_id")
            controller_port = gvl.controller_port  # Accessing controller_port from gvl.py
        
            print(f"Trying to connect to controller {controller_name} on net id {controller_net_id}...")
            try:
                plc = pyads.Connection(controller_net_id, port=controller_port)
                plc.open()
                # value set to gvl from plc
                gvl.parameter_list.controllers[controllerNum]["controllerObj"]= plc
                
                isControllerAvailable = plc_in.read_by_name('GVL.control_available',pyads.PLCTYPE_BOOL)
                print(isControllerAvailable)
            except:
                print("...unable to connect to controller")
                time.sleep(10)
                
             

                
                
                
def check_all_controller_availability(parameter_list, controller_port):

    connected_controllers = []
    disconnected_controllers=[]
    count = len(connected_controllers)
    while True:
        for controller_list in parameter_list.get("controllers", []):
            controller_name = controller_list.get("controller_name")
            controller_net_id = controller_list.get("controller_net_id")

            if controller_name not in connected_controllers and controller_name not in disconnected_controllers:
                try:
                    plc = pyads.Connection(controller_net_id, port=controller_port)
                    plc.open()
                    #plc.close()  # Close the connection after opening to check availability only
                    isControllerAvailable = plc_in.read_by_name('GVL.control_available',pyads.PLCTYPE_BOOL)
                    if isControllerAvailable:
                        connected_controllers.add(controller_name)
                    else:
                        disconnected_controllers.add(controller_name)
                            
                    print(f"Controller {controller_name} is now connected.")
                except pyads.ADSError as e:
                    #print(f"Controller {controller_name} is not available: {e}")
                    disconnected_controllers.add(controller_name)
                    return False  # Return False if any controller fails to connect
                except Exception as e:
                    print(f"An error occurred while connecting to controller {controller_name}: {e}")
                    disconnected_controllers.add(controller_name)
                    return False  # Return False if any other error occurs

        if count == len(parameter_list.get("controllers", [])):
            print("All controllers are connected.")
            return True  # Return True if all controllers are successfully connected
        else:
            #print("Attempting to connect to remaining controllers...")
            print(f"Connected controllers are {connected_controllers}")
            
            print(f"Disconnected controllers are {disconnected_controllers}")
            time.sleep(10)  # Sleep for some time before retrying

                        
            
            


# Example usage:
# check_controller_availability(gvl.parameter_list)