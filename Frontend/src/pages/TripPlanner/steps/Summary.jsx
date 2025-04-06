import React from "react";

const Summary = ({ tripData }) => {
  return (
    <div className="p-6 border rounded-2xl shadow-lg bg-gradient-to-br from-white to-gray-100">
      <h2 className="text-3xl font-extrabold text-gray-800 mb-5 border-b pb-2">✈️ Resumen de tu viaje</h2>

      <div className="space-y-3 text-lg text-gray-700">
        <p><strong className="text-indigo-600">🌍 Destino:</strong> {tripData.destination || "No seleccionado"}</p>
        <p><strong className="text-blue-600">🗓 Duración:</strong> {tripData.duration ? `${tripData.duration} días` : "No seleccionado"}</p>
        <p><strong className="text-green-600">🚆 Transporte:</strong> {tripData.transport || "No seleccionado"}</p>
        <p><strong className="text-orange-600">🎯 Tipo de turismo:</strong> {tripData.activities.length > 0 ? tripData.activities.join(", ") : "Ninguna seleccionada"}</p>
        <p><strong className="text-red-600">💰 Presupuesto:</strong> {tripData.budget || "No definido"}</p>
      </div>
    </div>
  );
};

export default Summary;
