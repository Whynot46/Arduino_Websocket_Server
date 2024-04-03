#include <SPI.h>
#include <Ethernet.h>
#include <WebSocket.h>


WebSocketServer wsServer;


byte mac[] = { 0x52, 0x4F, 0x43, 0x4B, 0x45, 0x54 };
byte ip[] = { 192, 168, 1 , 10 }; // Any IP address, according to your network adapter settings. Attention, there must be one subnet with the client!


void onConnect(WebSocket &socket) {
  Serial.println("onConnect called");
}


void onData(WebSocket &socket, char* dataString, byte frameLength) {
  // Just echo back data for fun.
  socket.send(dataString, strlen(dataString));
}


void onDisconnect(WebSocket &socket) {
  Serial.println("onDisconnect called");
}


int get_response_len(int value){
  int len = 0;
  
  for(int j=abs(value); j>0; j/=10){
    len++;
  }

  if(value<0){ // If the number is negative, space is added for the minus
    len++;
  }

  return len;
}


void setup() {
  Ethernet.begin(mac, ip);
  wsServer.registerConnectCallback(&onConnect);
  wsServer.registerDataCallback(&onData);
  wsServer.registerDisconnectCallback(&onDisconnect);  
  wsServer.begin();
  
  delay(10); // Give Ethernet time to get ready
}


void loop() {
  wsServer.listen();

  int value = random(1000); //For example, we will send random integer values.
  
  int response_len = get_response_len(value);
  
  char response[response_len];
  sprintf(response, "%d", value);

  Serial.print("Response: ");
  Serial.println(response);
  Serial.print("Response_len: ");
  Serial.println(response_len);
  Serial.print("Connections: ");
  Serial.println(wsServer.connectionCount());;
  
  if (wsServer.connectionCount() > 0) {
    wsServer.send(response, response_len);
  }
  
  delay(10);
}
