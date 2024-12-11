import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

// Import your components
import Login from './components/Auth/Login';
import Register from './components/Auth/Register';
import JobList from './components/Job/JobList';
import JobDetails from './components/Job/JobDetails';
import CreateJob from './components/Job/CreateJob';
import ApplyJob from './components/Application/ApplyJob';
import ApplicationDetails from './components/Application/ApplicationDetails';
import CompanyProfile from './components/Company/CompanyProfile';
import CreateCompany from './components/Company/CreateCompany';

const AppRoutes: React.FC = () => {
  return (
    <Router>
      <Routes>
        {/* Auth Routes */}
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />

        {/* Job Routes */}
        <Route path="/" element={<JobList />} />
        <Route path="/jobs/create" element={<CreateJob />} />
        <Route path="/jobs/:jobId" element={<JobDetails />} />

        {/* Application Routes */}
        <Route path="/applications/:jobId/apply" element={<ApplyJob />} />
        <Route path="/applications/:appId" element={<ApplicationDetails />} />

        {/* Company Routes */}
        <Route path="/companies/create" element={<CreateCompany />} />
        <Route path="/companies/:companyId" element={<CompanyProfile />} />
      </Routes>
    </Router>
  );
};

export default AppRoutes;
