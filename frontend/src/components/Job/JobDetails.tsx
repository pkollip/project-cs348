import React from 'react';
import { useParams } from 'react-router-dom';

interface JobDetailsParams {
  jobId?: string;
}

const JobDetails: React.FC = () => {
  const { jobId } = useParams() as JobDetailsParams;
  
  return (
    <div>
      <h2>Job Details (ID: {jobId})</h2>
      {/* Job details content goes here */}
    </div>
  );
};

export default JobDetails;
