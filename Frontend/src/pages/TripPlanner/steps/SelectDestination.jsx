import React, { useState } from "react";
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
    <div>
      <h2 className="text-lg font-medium mb-2">¿Qué destino prefieres?</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {destinations.map((city) => (
          <Place
            key={city.name}
            name={city.name}
            description={city.description}
            isSelected={tripData.destination === city.name}
            onSelect={() => {setTripData({...tripData, destination: city.name})}}
          />
        ))}
      </div>
    </div>
  );
};

export default SelectDestination;
