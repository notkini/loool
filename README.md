# Silent Disengagement Detection

Early detection of silent student disengagement using behavioral patterns and explainable AI.

## Problem
Education systems often detect failure only after students drop out or fail exams.  
However, disengagement begins weeks earlier through subtle behavioral changes that go unnoticed.

## Solution
This project analyzes student engagement timelines to detect early disengagement signals and generate explainable, human-centered intervention suggestions.

The focus is on:
- Behavioral patterns, not grades
- Early detection, not failure prediction
- Ethical, non-judgmental insights
- Human-in-the-loop intervention

## Architecture Overview
- Event-based engagement data
- Rule-based, explainable disengagement detection
- AI-generated explanations using Gemini
- Designed for deployment on Google Cloud with Vertex AI

## Technology Stack
- Python
- Google Cloud (Vertex AI – Gemini)
- Explainable rule-based detection
- Cloud-ready architecture

## Status
Core disengagement detection logic is complete.  
Gemini integration via Vertex AI is implemented in code and requires cloud authentication (ADC) when running locally.

This repository represents a functional prototype focused on design clarity, ethical AI usage, and scalable cloud architecture.
