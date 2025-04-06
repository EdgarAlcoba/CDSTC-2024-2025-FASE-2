import React, { useState } from "react";

const dayOptions = ["1", "2", "3", "4", "5", "6", "7"];

const SelectDays = ({ tripData, setTripData }) => {
  return (
    <div className="p-5 bg-white rounded-xl shadow-md">
      <h2 className="text-xl font-semibold text-gray-800">📅 ¿Cuántos días tienes disponibles?</h2>
      
      <div className="flex gap-3 mt-4 flex-wrap">
        {dayOptions.map((numdays) => (
          <button
            key={numdays}
            className={`px-4 py-2 rounded-lg border-2 font-medium transition-all duration-300
              ${tripData.duration === numdays 
                ? "bg-green-200 border-green-500 text-green-900 shadow-md"
                : "bg-gray-100 border-gray-300 text-gray-700 hover:bg-gray-200"
              }`}
            onClick={() => setTripData({ ...tripData, duration: numdays })}
          >
            {numdays} {numdays === "1" ? "día" : "días"}
          </button>
        ))}
      </div>
    </div>
  );
};

export default SelectDays;
