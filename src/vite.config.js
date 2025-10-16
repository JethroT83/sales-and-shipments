/** @see // https://vite.dev/config/ */
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'
import tailwindcss from '@tailwindcss/vite'
//import svgr from "vite-plugin-svgr";

export default defineConfig(({ mode }) => {
    return {
        base: '/static/',
        plugins: [
            react(),
            tailwindcss()
//            svgr()
        ],

        resolve: {
            alias: {
                '@Assets': path.resolve(__dirname, './resources/assets'),
                '@Css': path.resolve(__dirname, './resources/css'),
                '@Layouts': path.resolve(__dirname, './resources/js/Layouts'),
                '@Pages': path.resolve(__dirname, './resources/js/Pages'),
                '@Components': path.resolve(__dirname, './resources/js/Components'),
            },
        },

        cacheDir: '/tmp/vite-cache',   // keep cache off bind mount
        optimizeDeps: {
            force: true,
            include: [
                'react',
                'react-dom/client',     // not 'react-dom'
                '@inertiajs/react',
                '@inertiajs/core',
                'axios',
            ],
        },

        server: {
            host: '0.0.0.0',
            port: 5173,
            watch: {
                usePolling: true,
            },
            strictPort: true,
//            hmr: {
//                host: 'localhost',
//                port: 5173,
//                protocol: 'ws',
//                path: '/../',
//            },
            proxy: {
                '^/(api|admin|auth|login)': {
                    target: 'http://localhost:8000',
                    changeOrigin: true,
                }
            },
        },

    //    build: {
    //        outDir: path.resolve(__dirname, 'public'),
    //        emptyOutDir: true,
    //        manifest: true,
    //        rollupOptions: {
    //            input: {
    //                main: path.resolve(__dirname, './resources/js/app.jsx'),
    //                css: path.resolve(__dirname, './resources/css/app.css')
    //            },
    //            output: {
    //                entryFileNames: 'app.js',
    //                chunkFileNames: 'chunks/[name].js',
    //                assetFileNames: 'assets/[name][extname]',
    //            },
    //        },
    //    },
    }
});
