# Generatore di Testi Curiosi

## Overview

This is a Flask-based web application that generates engaging curiosity texts using Google's Gemini AI. The application is specifically designed to create content optimized for VoiceOver on iPhone and YouTube Shorts. Users can either input a custom topic or let the system randomly select one from a predefined list. The generated texts are crafted to be 100-150 words, natural-sounding, and suitable for audio narration.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

**Web Framework**: Flask-based architecture with a simple MVC pattern
- `app.py` serves as the main application controller
- `templates/index.html` provides the user interface
- `gemini_service.py` handles AI integration and topic management

**Frontend Design**: Bootstrap 5-based responsive interface with custom CSS
- Modern gradient background with glassmorphism effects
- Mobile-first responsive design optimized for various screen sizes
- Italian language interface with accessibility considerations

**AI Integration**: Google Gemini API integration for text generation
- Structured prompting system for consistent output quality
- Error handling and logging for API failures
- Content optimization for voice narration and short-form content

**Topic Management**: Dual-mode topic selection system
- Manual topic input for specific content needs
- Random topic selection from curated list of 15 engaging categories
- Topics focused on science, history, culture, and curiosities

**Session Management**: Flask session handling with configurable secret keys
- Environment-based configuration for security
- Flash messaging system for user feedback

## External Dependencies

**Google Gemini AI**: Primary text generation service
- Requires `GEMINI_API_KEY` environment variable
- Used for creating human-like, engaging curiosity texts

**Bootstrap 5**: Frontend UI framework via CDN
- Provides responsive grid system and component styling

**Font Awesome 6**: Icon library via CDN
- Enhances user interface with vector icons

**Flask Framework**: Core web application framework
- Handles routing, templating, and session management

**Python Standard Libraries**: 
- `os` for environment variable management
- `logging` for application monitoring and debugging
- `random` for topic selection functionality