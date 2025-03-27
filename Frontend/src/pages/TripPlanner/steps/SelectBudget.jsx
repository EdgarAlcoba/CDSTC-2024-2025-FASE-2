import React, { useState } from "react";

const budgetOptions = ["Bajo ($)", "Medio ($$)", "Alto ($$$)"];

const SelectBudget = ({ tripData, setTripData }) => {

  return (
    <div>
      <h2 className="text-lg font-medium">¿Cuál es tu presupuesto?</h2>
      
      <div className="flex gap-4 mt-3">
        {budgetOptions.map((budget) => (
          <button
            key={budget}
            className={`px-4 py-2 border rounded-lg ${
              tripData.budget === budget ? "bg-blue-100 border-blue-500" : ""
            }`}
            onClick={() => setTripData({...tripData, budget: budget})}
          >
            {budget}
          </button>
        ))}
      </div>
    </div>
  );
};

export default SelectBudget;
