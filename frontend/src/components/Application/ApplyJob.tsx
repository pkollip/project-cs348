import React, { useState } from 'react';
import { useParams } from 'react-router-dom';

interface ApplyJobParams {
  jobId?: string;
}

const ApplyJob: React.FC = () => {
  const { jobId } = useParams() as ApplyJobParams;
  const [resume, setResume] = useState<File | null>(null);
  const [applicationData, setApplicationData] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // Logic to submit application, e.g., API call
    console.log({ jobId, resume, applicationData });
  };

  return (
    <div>
      <h2>Apply for Job (ID: {jobId})</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Upload Resume:
          <input
            type="file"
            onChange={(e) => setResume(e.target.files ? e.target.files[0] : null)}
            required
          />
        </label>
        <label>
          Additional Information:
          <textarea
            value={applicationData}
            onChange={(e) => setApplicationData(e.target.value)}
          />
        </label>
        <button type="submit">Apply</button>
      </form>
    </div>
  );
};

export default ApplyJob;
