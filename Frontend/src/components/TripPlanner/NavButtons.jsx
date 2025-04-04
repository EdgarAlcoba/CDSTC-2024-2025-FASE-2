import React from 'react';

const NavButtons = ({ onBack, onNext, disabledNext, disabledBack, submitReady }) => {
  return (
    <div className="flex justify-center space-x-6 items-center mt-6">
      
      <button
        onClick={onBack}
        disabled={disabledBack}
        className={`px-6 py-2 rounded-lg font-medium transition-all duration-300
          ${disabledBack 
            ? "bg-gray-300 text-gray-400 cursor-not-allowed" 
            : "bg-gray-200 text-gray-700 hover:bg-gray-300"
          }`}
      >
        {'← Atrás'}
      </button>

      <button
        onClick={onNext}
        disabled={disabledNext}
        className={`px-6 py-2 rounded-lg font-medium transition-all duration-300
          ${disabledNext 
            ? "bg-gray-300 text-gray-400 cursor-not-allowed" 
            : "bg-green-500 text-white hover:bg-green-600"
          }`}
      >
        {submitReady ? "🚀 Organizar viaje" : "Siguiente →"}
      </button>
    </div>
  );
};

export default NavButtons;
