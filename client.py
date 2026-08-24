class SidewalkRobotLastMileZeroEmissionDeliveryClient:
    def dispatch_sidewalk_delivery_bot(self, merchant_address='Santa Monica Blvd, LA', delivery_distance_km=1.8, payload_kg=6.5):
        return {
            'bot_mission_id': 'coco_bot_5519',
            'assigned_robot_id': 'COCO_ROBOT_LA_082',
            'teleoperated_remote_human_oversight': True,
            'transit_duration_minutes': round((delivery_distance_km / 12.0) * 60, 1) + 4.0,
            'carbon_emissions_saved_vs_car_pct': 100.0,
            'merchant_delivery_cost_reduction_pct': 48.0,
            'lockbox_otp_secure_handover_code': '902144'
        }
