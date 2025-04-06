import React from "react";

const transportOptions = ["Tranvía", "Bicicleta", "Autobús", "Coche compartido", "Metro", "Taxi"];

const SelectTransport = ({ tripData, setTripData }) => {
  return (
    <div className="p-6 bg-white rounded-xl shadow-md">
      <h2 className="text-xl font-semibold text-gray-800 mb-4">🚗 ¿Cómo quieres desplazarte?</h2>

      <div className="flex flex-wrap gap-3">
        {transportOptions.map((transport) => (
          <button
            key={transport}
            className={`px-5 py-2 rounded-lg border-2 font-medium transition-all duration-300
              ${tripData.transport === transport
                ? "bg-green-200 border-green-500 text-green-900 shadow-md scale-105"
                : "bg-gray-100 border-gray-300 text-gray-700 hover:bg-gray-200"
              }`}
            onClick={() => setTripData({ ...tripData, transport })}
          >
            {transport}
          </button>
        ))}
      </div>
    </div>
  );
};

export default SelectTransport;
