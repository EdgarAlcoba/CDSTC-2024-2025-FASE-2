import React from 'react';

const NavButtons = ({ onBack, onNext, disabledNext, disabledBack, submitReady }) => {
  return (
    <div className="flex justify-center space-x-10 items-center">
      
      <button
        onClick={onBack}
        disabled={disabledBack}
        className="px-6 py-2 bg-gray-300 text-gray-700 rounded-lg hover:bg-gray-400 focus:outline-none"
      >
        {'Back'}
      </button>

      <button
        onClick={onNext}
        disabled={disabledNext}
        className={"px-6 py-2 bg-gray-300 text-gray-700 rounded-lg hover:bg-gray-400 focus:outline-none"}
      >
        {submitReady ? "Plan trip" : "Next"}
      </button>
    </div>
  );
};

export default NavButtons;
