import React, { useState } from 'react';
import axios from 'axios';

const Register: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [userType, setUserType] = useState('applicant');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      // Make the POST request to the backend
      const response = await axios.post('http://localhost:5000/auth/register', {
        email,
        password,
        user_type: userType,  // Assuming your backend expects `user_type` in snake_case
      });

      // Handle success (for example, redirect to login or show a success message)
      console.log('Registration successful:', response.data);
      setSuccess(true);  // Indicate successful registration
    } catch (error) {
      // Handle error (display error message)
      if (axios.isAxiosError(error) && error.response) {
        setError(error.response.data.message || 'Registration failed');
      } else {
        setError('An unknown error occurred');
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>Register</h2>
      {success ? (
        <p>Registration successful! Please <a href="/login">log in</a>.</p>
      ) : (
        <form onSubmit={handleSubmit}>
          <label>
            Email:
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </label>
          <label>
            Password:
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </label>
          <label>
            User Type:
            <select value={userType} onChange={(e) => setUserType(e.target.value)}>
              <option value="applicant">Applicant</option>
              <option value="company_rep">Company Representative</option>
            </select>
          </label>
          <button type="submit" disabled={loading}>
            {loading ? 'Registering...' : 'Register'}
          </button>
        </form>
      )}
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
};

export default Register;
