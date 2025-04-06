import React from "react";
import Place from "../../../components/TripPlanner/Place";

const destinations = [
  { name: "Aruba Central", description: "Una vibrante ciudad isleña." },
  { name: "Nimble Peak", description: "Ubicada en lo alto de una cadena montañosa." },
  { name: "Composable Cloud", description: "Una metrópolis futurista." },
  { name: "Ezmeral Valley", description: "Un valle verde y fértil, famoso por sus viñedos." },
  { name: "ProLiant Village", description: "Un encantador pueblo tecnológico." },
  { name: "Apollo Heights", description: "Una ciudad de rascacielos brillantes." },
  { name: "Simplicity Springs", description: "Una ciudad balneario rodeada de fuentes termales." },
  { name: "GreenLake Shores", description: "Ubicada a orillas de un inmenso lago esmeralda." },
  { name: "Alletra City", description: "Una metrópolis vibrante que nunca duerme." },
  { name: "HPE Innovation Hub", description: "El corazón de la tecnología y el progreso." },
];

const SelectDestination = ({ tripData, setTripData }) => {
  return (
    <div className="p-6 bg-white rounded-xl shadow-md mb-5">
      <h2 className="text-xl font-semibold text-center text-gray-800 mb-4">🌍 Selecciona tu destino</h2>
      
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        {destinations.map((city) => (
          <Place
            key={city.name}
            name={city.name}
            description={city.description}
            isSelected={tripData.destination === city.name}
            onSelect={() => setTripData({ ...tripData, destination: city.name })}
            className={`cursor-pointer p-4 border-2 rounded-lg transition-all duration-300
              ${tripData.destination === city.name 
                ? "bg-green-200 border-green-500 shadow-md scale-105"
                : "bg-gray-100 border-gray-300 hover:bg-gray-200"
              }`}
          />
        ))}
      </div>
    </div>
  );
};

export default SelectDestination;
