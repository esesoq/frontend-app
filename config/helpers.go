package frontend_app

import (
	"errors"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"
	"strings"
)

// GetProjectRoot returns the project root path based on the current working directory
func GetProjectRoot() (string, error) {
	wd, err := os.Getwd()
	if err != nil {
		return "", err
	}

	wd = filepath.Rel(os.Getenv("GOPATH"), wd)

	// If current directory is not within GOPATH, return the current directory
	if !strings.HasPrefix(wd, filepath.Join(os.Getenv("GOPATH"), "src")) {
		return wd, nil
	}

	// Otherwise, return the project root directory
	return filepath.Dir(wd), nil
}

// ReadFileContents reads the contents of a file
func ReadFileContents(filePath string) (string, error) {
	data, err := ioutil.ReadFile(filePath)
	if err != nil {
		return "", err
	}

	return string(data), nil
}

// GetEnvOrReturnError gets an environment variable and returns an error if it's not set
func GetEnvOrReturnError(envKey string) (string, error) {
	value := os.Getenv(envKey)
	if value == "" {
		return "", errors.New("environment variable not set: " + envKey)
	}
	return value, nil
}