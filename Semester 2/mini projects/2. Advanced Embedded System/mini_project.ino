#include <dht.h>
#include <LiquidCrystal_I2C.h>
dht DHT;
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  // put your setup code here, to run once:
  lcd.init();
  lcd.backlight();
}

void loop() {
  // put your main code here, to run repeatedly:
  int chk = DHT.read(7);
  lcd.setCursor(0, 0);
  lcd.print("Temp.:");
  lcd.setCursor(10, 0);
  lcd.print(DHT.temperature);
  lcd.setCursor(0, 1);
  lcd.print("Humidity:");
  lcd.setCursor(10, 1);
  lcd.print(DHT.humidity);

}
