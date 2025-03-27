import React, { useState } from "react";

const activities = ["Cultural", "De aventura", "Gastronómico", "Histórico", "Ecológico"];

const SelectActivities = ({ tripData, setTripData }) => {

  const toggleActivity = (activity) => {
    const updatedActivities = tripData.activities.includes(activity)
      ? tripData.activities.filter((a) => a !== activity)
      : [...tripData.activities, activity];

    setTripData({ ...tripData, activities: updatedActivities });
  };

  return (
    <div>
      <h2 className="text-lg font-medium">¿Qué tipo de turismo buscas?</h2>
      <div className="flex flex-wrap gap-3 mt-3">
        {activities.map((activity) => (
          <button
            key={activity}
            className={`px-4 py-2 border rounded-lg ${
              tripData.activities.includes(activity) ? "bg-blue-100 border-blue-500" : ""
            }`}
            onClick={() => {toggleActivity(activity)}}
          >
            {activity}
          </button>
        ))}
      </div>
    </div>
  );
};

export default SelectActivities;
