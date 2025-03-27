import React from "react";

const Summary = ({ tripData }) => {
  return (
    <div className="p-5 border rounded-lg shadow-md bg-white">
      <h2 className="text-2xl font-bold mb-4">Resumen de tu viaje</h2>

      <p><strong>🌍 Destino:</strong> {tripData.destination || "No seleccionado"}</p>
      <p><strong>🚆 Transporte:</strong> {tripData.transport || "No seleccionado"}</p>
      <p><strong>🎯 Tipo de turismo:</strong> {tripData.activities.length > 0 ? tripData.activities.join(", ") : "Ninguna seleccionada"}</p>
      <p><strong>💰 Presupuesto:</strong> {tripData.budget || "No definido"}</p>
    </div>
  );
};

export default Summary;
