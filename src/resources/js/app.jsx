// @see https://github.com/BrandonShar/inertia-rails-template/blob/main/app/frontend/entrypoints/application.jsx
import '@Css/app.css';
import React from 'react'
import { createRoot } from 'react-dom/client'
import { createInertiaApp } from '@inertiajs/react'

console.log('boot app.jsx')

const pages = import.meta.glob('./Pages/**/*.jsx', { eager: true })

createInertiaApp({
  resolve: name => {
    const page = pages[`./Pages/${name}.jsx`]
    if (!page) throw new Error(`Page not found: ${name}`)
    return page
  },
  setup({ el, App, props }) {
    createRoot(el).render(<App {...props} />)
  },
})