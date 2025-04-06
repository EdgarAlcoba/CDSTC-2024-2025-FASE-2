import { Canvas } from "@react-three/fiber";
import { Experience } from "./Experience";
import { Loader } from "@react-three/drei";

const PlannerResult = () => {
  const cameraSpecs = {
    "Aruba Central": {
      fov: 104,
      position: [2.8, 1.5, 3.3],
    },
    "Nimble Peak": {
      fov: 84,
      position: [0.40, 0.3, 0.4],
    },
    "Composable Cloud": {
      fov: 54,
      position: [0.3, 1.0, 1.8],
    },
    "Ezmeral Valley": {
      fov: 84,
      position: [2.3, 2.0, 2.3],
    },
    "ProLiant Village": {
      fov: 94,
      position: [2.3, 2.0, 2.3],
    },
    "Apollo Heights": {
      fov: 84,
      position: [2.3, 2.0, 2.3],
    },
    "Simplivity Springs": {
      fov: 84,
      position: [2.3, 2.0, 2.3],
    },
    "GreenLake Shores": {
      fov: 74,
      position: [1.0, 0.4, 1.0],
    },
    "Alletra City": {
      fov: 74,
      position: [100.0, 40.0, 100.0],
    },
    "HPE Innovation Hub": {
      fov: 34,
      position: [1.2, 0.8, 0.9],
    },
  };

  const data = JSON.parse(`{
  "destination": "Aruba Central",
  "duration": 3,
  "budget": "High",
  "itinerary": [
    {
      "day": 1,
      "activities": [
        {
          "time": "09:00 AM",
          "activity": "Check-in at Aruba Luxury Lodge",
          "details": "Enjoy a complimentary welcome drink and a brief tour of the amenities.",
          "location": "Aruba Luxury Lodge"
        },
        {
          "time": "11:00 AM",
          "activity": "Bicycle Tour of Arikok National Park",
          "details": "Guided cycling adventure through rugged terrains and stunning landscapes.",
          "location": "Arikok National Park"
        },
        {
          "time": "02:00 PM",
          "activity": "Lunch at Elements Restaurant",
          "details": "Enjoy a gourmet meal with a focus on organic and local ingredients.",
          "location": "Elements Restaurant"
        },
        {
          "time": "04:00 PM",
          "activity": "Snorkeling Adventure",
          "details": "Discover the vibrant marine life in crystal clear waters.",
          "location": "Mangel Halto"
        },
        {
          "time": "07:00 PM",
          "activity": "Dinner at Passions on the Beach",
          "details": "Dine under the stars with a beautiful sunset view.",
          "location": "Passions on the Beach"
        }
      ]
    },
    {
      "day": 2,
      "activities": [
        {
          "time": "09:30 AM",
          "activity": "Bicycle to the Butterfly Farm",
          "details": "Experience the tranquility of wandering through a tropical garden with butterflies.",
          "location": "The Butterfly Farm"
        },
        {
          "time": "12:00 PM",
          "activity": "Lunch at Yemanja Woodfired Grill",
          "details": "Taste the exotic flavors and wood-fired dishes.",
          "location": "Yemanja Woodfired Grill"
        },
        {
          "time": "02:30 PM",
          "activity": "Bicycle to Alto Vista Chapel",
          "details": "Visit the historical and spiritual chapel and enjoy the serene surroundings.",
          "location": "Alto Vista Chapel"
        },
        {
          "time": "06:00 PM",
          "activity": "Sunset Sailing Excursion",
          "details": "Luxury catamaran tour with cocktails and snacks.",
          "location": "Palm Beach Marina"
        },
        {
          "time": "08:30 PM",
          "activity": "Dinner at Barefoot Restaurant",
          "details": "Fine dining with your toes in the sand.",
          "location": "Barefoot Restaurant"
        }
      ]
    },
    {
      "day": 3,
      "activities": [
        {
          "time": "10:00 AM",
          "activity": "Bicycle to Ayo and Casibari Rock Formations",
          "details": "Explore fascinating rock formations and enjoy panoramic views.",
          "location": "Ayo and Casibari"
        },
        {
          "time": "01:00 PM",
          "activity": "Gourmet Lunch at The Kitchen Table",
          "details": "Indulgent lunch with a chef's tasting menu.",
          "location": "The Kitchen Table"
        },
        {
          "time": "03:00 PM",
          "activity": "Relax at Eagle Beach",
          "details": "Unwind on one of the world's most beautiful beaches.",
          "location": "Eagle Beach"
        },
        {
          "time": "06:00 PM",
          "activity": "Farewell Dinner at Quinta del Carmen",
          "details": "Enjoy an intimate dining experience in a historic mansion.",
          "location": "Quinta del Carmen"
        }
      ]
    }
  ]
}`)

  const camera = cameraSpecs[data.destination] || [];

  return (
    <div style={{ height: "100dvh", width: "100dvw" }}>
      <Loader />
      <Canvas
        camera={{
          fov: camera.fov,
          position: camera.position,
        }}
      >
        <Experience city={data.destination} data={data} />
      </Canvas>
    </div>
  );
};

export default PlannerResult;
