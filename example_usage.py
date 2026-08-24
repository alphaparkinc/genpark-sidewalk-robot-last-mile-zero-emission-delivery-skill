from client import SidewalkRobotLastMileZeroEmissionDeliveryClient

def main():
    client = SidewalkRobotLastMileZeroEmissionDeliveryClient()
    res = client.dispatch_sidewalk_delivery_bot('Venice Beach, CA', 2.4, 4.0)
    print('Bot Mission: ' + res['bot_mission_id'] + ' (' + res['assigned_robot_id'] + ')')
    print('Transit Time: ' + str(res['transit_duration_minutes']) + ' mins (Carbon Saved: ' + str(res['carbon_emissions_saved_vs_car_pct']) + '%)')
    print('Merchant Delivery Cost: -' + str(res['merchant_delivery_cost_reduction_pct']) + '% | Lockbox OTP: ' + res['lockbox_otp_secure_handover_code'])

if __name__ == '__main__':
    main()
