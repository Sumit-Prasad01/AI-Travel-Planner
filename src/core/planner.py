from langchain_core.messages import HumanMessage, AIMessage
from src.chains.itineary_chain import generate_itineary
from src.utils.custom_exception import CustomException
from src.utils.logger import get_logger

logger = get_logger(__name__)


class TravelPlanner:

    def __init__(self):
        
        self.messages = []
        self.city = ""
        self.interests = []
        self.itineary = ""

        logger.info("Initialized travel planner instance.")

    
    def set_city(self, city : str):
        try:

            self.city = city
            self.messages.append(HumanMessage(content = city))

            logger.info("City seted successfully.")
        
        except Exception as e:
            logger.error(f"Error while setting up city : {e}")
            raise CustomException("Failed to set city : ", e)
    

    def set_interests(self, interests_str : str):
        try:

            self.interests = [i.strip() for i in interests_str.split(",")]
            self.messages.append(HumanMessage(content = interests_str))

            logger.info("Interests seted successfully.")
        
        except Exception as e:
            logger.error(f"Error while setting up interests : {e}")
            raise CustomException("Failed to set interests : ", e)
    

    def create_itineary(self):
        try:

            logger.info(f"Generating itineary for city : {self.city} and for interests : {self.interests}")

            itineary = generate_itineary(self.city, self.interests)
            self.itineary = itineary
            self.messages.append(AIMessage(content = itineary))

            logger.info("Itineary generated successfully.")

            return self.itineary
        
        except Exception as e:
            logger.error(f"Error while generating itineary : {e}")
            raise CustomException("Failed to generate itineary : ", e)