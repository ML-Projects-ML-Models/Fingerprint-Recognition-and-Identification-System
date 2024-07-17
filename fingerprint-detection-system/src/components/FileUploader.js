// src/components/FileUploader.js
import React, { useEffect, useState } from 'react';
import { Container, Box, Button, Typography } from '@mui/material';
import { motion } from 'framer-motion';
import './FileUploader.css';

const FileUploader = () => {
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = () => {
    if (file) {
      const apiUrl = 'YOUR_API_ENDPOINT'; // Replace with your actual API endpoint
      const formData = new FormData();
      formData.append('file', file);

      fetch(apiUrl, {
        method: 'POST',
        body: formData,
      })
        .then((response) => response.json())
        .then((data) => {
          console.log('Success:', data);
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    }
  };

  useEffect(() => {
    const createCubes = () => {
      const cube = document.createElement('div');
      cube.className = 'cube';
      cube.style.left = `${Math.random() * 100}vw`;
      cube.style.animationDuration = `${Math.random() * 3 + 2}s`;
      document.body.appendChild(cube);

      setTimeout(() => {
        cube.remove();
      }, 5000);
    };

    const interval = setInterval(createCubes, 300);
    return () => clearInterval(interval);
  }, []);

  return (
    <Container className="hacker-theme">
      <Box
        display="flex"
        flexDirection="column"
        alignItems="center"
        justifyContent="center"
        height="100vh"
      >
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 1 }}
          className="glitch"
          data-text="Fingerprint Detection System"
        >
          Fingerprint Detection System
        </motion.div>
        <motion.div
          initial={{ opacity: 0, scale: 0.8 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.5 }}
        >
          <Button
            variant="contained"
            component="label"
            className="hacker-button"
            sx={{ mb: 3 }}
          >
            Choose File
            <input
              type="file"
              hidden
              onChange={handleFileChange}
            />
          </Button>
          {file && <Typography variant="body1" className="hacker-text">{file.name}</Typography>}
          <Button
            variant="contained"
            onClick={handleUpload}
            disabled={!file}
            className="hacker-button"
          >
            Upload
          </Button>
        </motion.div>
      </Box>
    </Container>
  );
};

export default FileUploader;
