int petFoodDispenser = D5;
int times =1;
void setup()
{

   pinMode(petFoodDispenser, OUTPUT);


   Particle.function("led",ledToggle);

   digitalWrite(petFoodDispenser, LOW);

}

void loop()
{

}

int ledToggle(String command) {

    if (command=="FoodDispenserON") {
        digitalWrite(petFoodDispenser,HIGH);
        Particle.publish("Meals",(String)times,PRIVATE);
        delay(5000);
        digitalWrite(petFoodDispenser,LOW);
        times = times+1;
        return 1;
    }

    
    else if (command=="FoodDispenserOFF") {
        digitalWrite(petFoodDispenser,HIGH);
        delay(100);
        digitalWrite(petFoodDispenser,LOW);
        delay(100);
        digitalWrite(petFoodDispenser,HIGH);
        delay(100);
        digitalWrite(petFoodDispenser,LOW);
        delay(100);
        digitalWrite(petFoodDispenser,HIGH);
        delay(100);
        digitalWrite(petFoodDispenser,HIGH);
        delay(100);
        digitalWrite(petFoodDispenser,LOW);
        delay(100);
        digitalWrite(petFoodDispenser,HIGH);
        delay(100);
        digitalWrite(petFoodDispenser,LOW);
        delay(100);
        digitalWrite(petFoodDispenser,HIGH);
        delay(100);
        digitalWrite(petFoodDispenser,LOW);
        return 0;
    }

    else 
    {
        return -1;
    }
}
