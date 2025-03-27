import React, { useState } from "react";

const transportOptions = ["Tranvía", "Bicicleta", "Autobús", "Coche compartido", "Metro", "Taxi"];

const SelectTransport = ({ tripData, setTripData }) => {
  const [selected, setSelected] = useState(null);

  return (
    <div>
      <h2 className="text-lg font-medium">¿Cómo quieres desplazarte?</h2>
      <div className="flex gap-4 mt-3">
        {transportOptions.map((transport) => (
          <button
            key={transport}
            className={`px-4 py-2 border rounded-lg ${
              tripData.transport === transport ? "bg-blue-100 border-blue-500" : ""
            }`}
            onClick={() => {setTripData({...tripData, transport: transport})}}
          >
            {transport}
          </button>
        ))}
      </div>
    </div>
  );
};

export default SelectTransport;
