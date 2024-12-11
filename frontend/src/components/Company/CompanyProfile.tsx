import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

interface CompanyProfileParams {
  companyId: string;
}

interface CompanyData {
  company_name: string;
  description: string;
  website: string;
  location: string;
  industry: string;
}

const CompanyProfile: React.FC = () => {
  const { companyId } = useParams() as unknown as CompanyProfileParams;
  const [company, setCompany] = useState<CompanyData | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchCompanyData = async () => {
      try {
        setLoading(true);
        setError(null);
        
        // Fetch data from the API
        const response = await axios.get<CompanyData>(`http://localhost:5000/company/${companyId}`);
        
        setCompany(response.data);
      } catch (error) {
        setError('Failed to fetch company data.');
        console.error(error);
      } finally {
        setLoading(false);
      }
    };

    fetchCompanyData();
  }, [companyId]);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>{error}</p>;

  return (
    <div>
      <h2>Company Profile</h2>
      {company && (
        <div>
          <h3>{company.company_name}</h3>
          <p><strong>Description:</strong> {company.description}</p>
          <p><strong>Website:</strong> <a href={company.website} target="_blank" rel="noopener noreferrer">{company.website}</a></p>
          <p><strong>Location:</strong> {company.location}</p>
          <p><strong>Industry:</strong> {company.industry}</p>
        </div>
      )}
    </div>
  );
};

export default CompanyProfile;
