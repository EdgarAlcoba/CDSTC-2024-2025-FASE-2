import React, { useState } from "react";

const Place = ({ name, description, onSelect, isSelected }) => {
  return (
    <button
      onClick={onSelect}
      className={`border rounded-lg p-5 shadow-md transition text-left ${
        isSelected ? "border-blue-500 bg-blue-100" : "hover:shadow-lg"
      }`}
    >
      <h3 className="text-lg font-semibold">{name}</h3>
      <p className="text-gray-600 mt-2 text-sm">{description}</p>
    </button>
  );
};

export default Place;
