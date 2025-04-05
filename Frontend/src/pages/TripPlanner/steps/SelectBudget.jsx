import React from "react";

const budgetOptions = ["Bajo", "Medio", "Alto"];

const SelectBudget = ({ tripData, setTripData }) => {
  return (
    <div className="p-6 bg-white rounded-xl shadow-md">
      <h2 className="text-xl font-semibold text-gray-800 mb-4">💰 ¿Cuál es tu presupuesto?</h2>
      
      <div className="flex gap-3">
        {budgetOptions.map((budget) => (
          <button
            key={budget}
            className={`px-5 py-2 rounded-lg border-2 font-medium transition-all duration-300
              ${tripData.budget === budget
                ? "bg-green-200 border-green-500 text-green-900 shadow-md scale-105"
                : "bg-gray-100 border-gray-300 text-gray-700 hover:bg-gray-200"
              }`}
            onClick={() => setTripData({ ...tripData, budget })}
          >
            {budget}
          </button>
        ))}
      </div>
    </div>
  );
};

export default SelectBudget;
