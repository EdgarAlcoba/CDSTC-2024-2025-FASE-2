import React, { useState } from "react";

const Place = ({ name, description, onSelect, isSelected }) => {
  return (
    <button
      onClick={onSelect}
      className={`border rounded-lg p-5 shadow-md transition text-left ${
        isSelected ? "border-emerald bg-tea-green" : "hover:shadow-lg"
      }`}
    >
      <h3 className="text-base font-semibold">{name}</h3>
      <p className="text-gray-500 mt-2 text-sm">{description}</p>
    </button>
  );
};

export default Place;
