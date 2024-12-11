import React from 'react';
import { useParams } from 'react-router-dom';

interface ApplicationDetailsParams {
  appId?: string;
}

const ApplicationDetails: React.FC = () => {
  const { appId } = useParams() as ApplicationDetailsParams;

  return (
    <div>
      <h2>Application Details (ID: {appId})</h2>
      {/* Application details content goes here */}
    </div>
  );
};

export default ApplicationDetails;
