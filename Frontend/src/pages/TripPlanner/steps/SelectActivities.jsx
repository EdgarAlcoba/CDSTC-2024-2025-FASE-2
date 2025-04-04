import React from "react";

const activities = ["Cultural", "De aventura", "Gastronómico", "Histórico", "Ecológico"];

const SelectActivities = ({ tripData, setTripData }) => {

  const toggleActivity = (activity) => {
    const updatedActivities = tripData.activities.includes(activity)
      ? tripData.activities.filter((a) => a !== activity)
      : [...tripData.activities, activity];

    setTripData({ ...tripData, activities: updatedActivities });
  };

  return (
    <div className="p-6 bg-white rounded-xl shadow-md">
      <h2 className="text-xl font-semibold text-gray-800 mb-4">🎯 ¿Qué tipo de turismo buscas?</h2>

      <div className="flex flex-wrap gap-3">
        {activities.map((activity) => (
          <button
            key={activity}
            className={`px-5 py-2 rounded-lg border-2 font-medium transition-all duration-300
              ${tripData.activities.includes(activity)
                ? "bg-green-200 border-green-500 text-green-900 shadow-md scale-105"
                : "bg-gray-100 border-gray-300 text-gray-700 hover:bg-gray-200"
              }`}
            onClick={() => toggleActivity(activity)}
          >
            {activity}
          </button>
        ))}
      </div>
    </div>
  );
};

export default SelectActivities;
