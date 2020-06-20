import logging
import json

from pyIndego import IndegoClient

logging.basicConfig(filename='pyIndego.log',level=logging.DEBUG)
_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.DEBUG)


def main(config):
    with IndegoClient(**config) as indego:
        #indego.update_network()
        #print(indego.network)
        # indego.update_all(force=True)
        # print(indego)
        indego.update_generic_data()
        indego.update_state()
        #print(indego.generic_data)
        print("=[state]====")
        print(indego.state)
        print("=[state.state]====")
        print(indego.state.state)
        print("=[state_description]====")
        print(indego.state_description)

        # indego.update_last_completed_mow()
        # indego.update_location()
        # indego.update_next_mow()
        # indego.update_operating_data()
        # # indego.update_updates()
        # # indego.update_users()
        # # indego.update_network()
        # indego.download_map()
        # indego.update_longpoll_state(120)
        # indego.update_alerts()
        # print("map: ", indego.map_filename)
        # print("network ", indego.network)
        # print("state: ", indego.state)
        # print("users: ", indego.users)
        # print("Generic data: ", indego.generic_data)
        print("Generic data min voltage: ", indego.generic_data.model_voltage.min)
        # print("Alerts: ", indego.alerts)
        # print("Operating_data: ", indego.operating_data)
        # print("Battery: ", indego.operating_data.battery)
        # # indego.update_generic_data()
        # print("Battery: ", indego.operating_data.battery)
        # print("Session charge: ", indego.operating_data.runtime.session.charge)

        # print("Next mow: ", indego.next_mow)
        # print("location: ", indego.location)
        # print("last mow: ", indego.last_completed_mow)
        # print(indego.generic_data.alm_mode)
        # print(indego.alm_name)
        # print(indego.service_counter)
        # print(indego.needs_service)
        # print(indego.alm_mode)
        # print(indego.bare_tool_number)
        # print(indego.alm_firmware_version)
        # print(indego.model_description)
        # print(indego.model_voltage)
        # print(indego.mowing_mode_description)
        # print(indego.model_description)
        # print(indego.model_description)
        # print(indego.mower_state)
        # print(indego.mower_state_description)
        # print(indego.mower_state_description_detailed)
        # print(indego.battery)
        # print(indego.alerts_count)
        # print(indego.email)
        # print(indego.garden)
        # print(indego.x_pos, ", ", indego.y_pos)
        # indego.show_vars()


if __name__ == "__main__":
    with open("config.json", "r") as config_file:
        config = json.load(config_file)
    main(config)
