#include <SoftwareSerial.h>
#include <OneWire.h>

SoftwareSerial BTSerial(2,3); // 아두이노에 블루투스 모듈의 TX, RX를 연결

float now_temp;//현재 온도
int set_temp; //설정 온도
int TS = 4; //온도센서
OneWire ds(TS);
int CO = 7; //초음파 출력
int CI = 6; //초음파 입력
int R=9;
int G=10;
int B=11;
int HEAT = 13; // 열선
long CHP_DELAY_TIME = 1000000; //1초 (마이크로세컨->세컨)

int now_temp_compare=0; //비교
boolean POWERON = false; //처음 작동시 B LED의 FLAG.

void setup() {
  BTSerial.begin(9600); // 아두이노의 시리얼 전송속도와 블루투스의 데이터 전송속도를 같게 해 줌
  analogReference(DEFAULT); //5V 설정
  pinMode(CO,OUTPUT);//초음파 센서 지정
  pinMode(CI,INPUT); //초음파 센서 지정
  pinMode(R,OUTPUT); //R LED
  pinMode(G,OUTPUT); //G LED
  pinMode(B,OUTPUT); //B LED
  pinMode(HEAT,OUTPUT); //열선
  pinMode(8, OUTPUT);
}

void loop() {
  float distance = CupCheck(); //초음파로 컵 유무 체크
  
  if (distance < 4 && POWERON == false){ //파란불 3회 점멸.
    PowerOn(); 
  }
  
  if (distance < 4 && POWERON == true){ //컵 끼워짐.
    digitalWrite(8, HIGH);
    delay(1500);
    now_temp = getTemp(); //센서에서 읽은 전압 값 온도로 변환후 저장.
    set_temp = RecieveTemp(); //핸드폰에서 설정 온도 받기.
    SendTemp(now_temp); //현재 온도를 핸드폰으로 보내기.
    ManageHeat(set_temp,(int)now_temp); //열선 ON/OFF
  }
  else if (distance > 4 ){ //컵 빠짐
       digitalWrite(8, LOW);
       delay(1500);
       if (POWERON != false){
       PowerOff(); //LED 끄기 (RGB순으로 점멸후 점등)
       }
       digitalWrite(HEAT, LOW); //열선 끄기
    }  
}

float CupCheck(){
  delayMicroseconds(2*CHP_DELAY_TIME); //2초 주기로 반복 확인
  digitalWrite(CO, LOW);
  digitalWrite(CI, LOW);
  delayMicroseconds(2);
  digitalWrite(CO, HIGH);
  delayMicroseconds(10);
  digitalWrite(CO, LOW); //초음파 거리측정
  unsigned long duration = pulseIn(CI, HIGH);
  float distance = duration / 29.0 / 2.0; //초음파 거리

  return distance;
}

void PowerOn(){
  for (int i=0; i<3; i++){
    analogWrite(R, 0);
    analogWrite(G, 0);
    analogWrite(B, 255);
    delay(500);
    analogWrite(R, 0);
    analogWrite(G, 0);
    analogWrite(B, 0);
    delay(500);
  }
  POWERON = true;
}

void PowerOff(){
    analogWrite(R, 255);
    analogWrite(G, 0);
    analogWrite(B, 0);
    delay(1000);
    analogWrite(R, 0);
    analogWrite(G, 255);
    analogWrite(B, 0);
    delay(1000);
    analogWrite(R, 0);
    analogWrite(G, 0);
    analogWrite(B, 255);
    delay(1000);
    analogWrite(R, 0);
    analogWrite(G, 0);
    analogWrite(B, 0);
    POWERON = false;    
}


float getTemp()
{
  byte data[12];
  byte addr[8];
  if ( !ds.search(addr))
  {
      ds.reset_search();
      return -1000;
  }

  if ( OneWire::crc8( addr, 7) != addr[7])
  {
      Serial.println("CRC is not valid!");
      return -1000;
  }
  if ( addr[0] != 0x10 && addr[0] != 0x28)
  {
      Serial.print("Device is not recognized");
      return -1000;
  }

  ds.reset();
  ds.select(addr);
  ds.write(0x44,1); 

  byte present = ds.reset();
  ds.select(addr);    
  ds.write(0xBE);
  
  for (int i = 0; i < 9; i++)
  { 
    data[i] = ds.read();
  }
  
  ds.reset_search();
  
  byte MSB = data[1];
  byte LSB = data[0];

  float tempRead = ((MSB << 8) | LSB); 
  float TemperatureSum = tempRead / 16;
  
  return TemperatureSum;
}

int RecieveTemp(){
  if(BTSerial.available()) {  
      int settemp = BTSerial.read();   //설정할 온도 수신.
      return settemp;
    }
  else{
      return set_temp;
    }
}

void SendTemp(float nowtemp){
  if (now_temp_compare != (int) nowtemp){ //현재 온도 전송.
       BTSerial.write((int)nowtemp); 
       now_temp_compare = (int)nowtemp;
    }
}

void ManageHeat(int settemp, int nowtemp){
  if (nowtemp <(settemp-5)){
    digitalWrite(HEAT, HIGH);
    analogWrite(R, 128);
    analogWrite(G, 128);
    analogWrite(B, 0);    
  }
  else if (nowtemp> (settemp+5)){
    digitalWrite(HEAT, LOW);
    analogWrite(R, 128);
    analogWrite(G, 0);
    analogWrite(B, 128);    
  }
}

