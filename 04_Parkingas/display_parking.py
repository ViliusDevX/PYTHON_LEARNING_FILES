import cv2
import numpy as np


def display_background_and_car(self):
        parking_lot_image = self.frame.copy()

        for lot_num in range(len(self.parking_inst.spaces)):
            car = self.parking_inst.spaces[lot_num]
            if car is not None:
                car_x = 100 * lot_num
                car_y = 0

                car_height, car_width, _ = self.car.shape

                if car_x + car_width <= parking_lot_image.shape[1] and car_y + car_height <= parking_lot_image.shape[0]:
                    car_image = self.car[:, :, :3]
                    car_alpha = self.car[:, :, 3] / 255.0
                    car_image = cv2.resize(car_image, (car_width, car_height))
                    car_alpha = cv2.resize(car_alpha, (car_width, car_height))

                    parking_lot_image[car_y:car_y + car_height, car_x:car_x + car_width] = (
                        (1 - car_alpha)[:, :, np.newaxis] * parking_lot_image[car_y:car_y + car_height, car_x:car_x + car_width] +
                        (car_alpha)[:, :, np.newaxis] * car_image
                    )

                    stay_time = car.get_stay_time()
                    payment = car.get_payment(park.rate_per_minute)

                    car_number = car.return_number()
                    text_color = (0, 0, 0)
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    font_scale = 0.5
                    font_thickness = 1

                    stay_time_text = f"{stay_time} sec"
                    payment_text = f"{payment} EUR"
                    stay_time_size = cv2.getTextSize(stay_time_text, font, font_scale, font_thickness)[0]
                    payment_size = cv2.getTextSize(payment_text, font, font_scale, font_thickness)[0]

                    text_x = car_x + (car_width - max(stay_time_size[0], payment_size[0])) // 2
                    text_y = car_y + car_height + 20

                    cv2.putText(parking_lot_image, car_number, (text_x, text_y), font, font_scale, text_color, font_thickness)

                    text_y += 20
                    cv2.putText(parking_lot_image, stay_time_text, (text_x, text_y), font, font_scale, text_color, font_thickness)

                    text_y += 20
                    cv2.putText(parking_lot_image, payment_text, (text_x, text_y), font, font_scale, text_color, font_thickness)

        text = f"Uzdarbis : {self.parking_inst.total_lot_price}"
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        font_color = (255, 255, 255)
        font_thickness = 2
        x, y = 270, 270
        cv2.putText(parking_lot_image, text, (x, y), font, font_scale, font_color, font_thickness)

        cv2.imshow("Parking Lot with Car and Text", parking_lot_image)
        cv2.waitKey(1)