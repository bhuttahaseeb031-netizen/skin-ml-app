<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DermaAI | Next-Gen Skin Health & Cancer Predictor</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        body {
            background: radial-gradient(circle at top left, #0f172a, #1e293b, #090d16);
            color: #f8fafc;
            font-family: 'Inter', system-ui, -apple-system, sans-serif;
            min-height: 100vh;
        }
        .glass-card {
            background: rgba(30, 41, 59, 0.7);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        }
        .gradient-text {
            background: linear-gradient(90deg, #38bdf8, #818cf8, #c084fc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .upload-zone {
            border: 2px dashed rgba(56, 189, 248, 0.4);
            transition: all 0.3s ease;
        }
        .upload-zone:hover {
            border-color: #38bdf8;
            background: rgba(56, 189, 248, 0.05);
        }
    </style>
</head>
<body class="p-4 md:p-8">

    <!-- Navbar -->
    <nav class="max-w-6xl mx-auto flex justify-between items-center mb-10">
        <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-sky-500/20 border border-sky-400/30 flex items-center justify-center text-sky-400">
                <i class="fa-solid fa-microscope text-xl"></i>
            </div>
            <span class="text-xl font-bold tracking-tight">Derma<span class="text-sky-400">AI</span></span>
        </div>
        <span class="text-xs px-3 py-1 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
            <i class="fa-solid fa-circle text-[8px] mr-1.5 animate-pulse"></i> AI Diagnostic Engine v2.4
        </span>
    </nav>

    <!-- Main Container -->
    <main class="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-12 gap-8">
        
        <!-- Left Column: Image Upload & Preview -->
        <div class="lg:col-span-5 space-y-6">
            <div class="glass-card rounded-3xl p-6">
                <h2 class="text-lg font-semibold mb-1 flex items-center gap-2">
                    <i class="fa-solid fa-camera-retro text-sky-400"></i> 1. Dermoscopy Image
                </h2>
                <p class="text-slate-400 text-xs mb-5">Upload a clear, well-lit macro photo of the skin area.</p>

                <label for="skinImage" class="upload-zone rounded-2xl p-8 flex flex-col items-center justify-center cursor-pointer text-center relative overflow-hidden min-h-[260px]">
                    <div id="uploadPrompt">
                        <div class="w-14 h-14 rounded-full bg-sky-500/10 text-sky-400 flex items-center justify-center mx-auto mb-3">
                            <i class="fa-solid fa-cloud-arrow-up text-2xl"></i>
                        </div>
                        <p class="text-sm font-medium text-slate-200">Click to upload or drag & drop</p>
                        <p class="text-xs text-slate-500 mt-1">JPG, JPEG, PNG (Max 200MB)</p>
                    </div>
                    <img id="imagePreview" class="hidden w-full h-60 object-cover rounded-xl" alt="Skin Preview" />
                    <input type="file" id="skinImage" accept="image/png, image/jpeg, image/jpg" class="hidden" onchange="previewFile(event)">
                </label>

                <div class="mt-4 p-3 rounded-xl bg-amber-500/10 border border-amber-500/20 text-amber-300 text-xs flex gap-2.5">
                    <i class="fa-solid fa-triangle-exclamation mt-0.5"></i>
                    <span>For optimal accuracy, ensure no shadows or filters cover the lesion.</span>
                </div>
            </div>
        </div>

        <!-- Right Column: Patient & Lifestyle Form -->
        <div class="lg:col-span-7">
            <div class="glass-card rounded-3xl p-6 md:p-8">
                <h1 class="text-2xl md:text-3xl font-bold gradient-text mb-2">Skin Health & Cancer Predictor</h1>
                <p class="text-slate-400 text-sm mb-6">Combine visual AI screening with patient lifestyle metrics for a comprehensive risk profile.</p>

                <form id="predictorForm" onsubmit="generateReport(event)" class="space-y-5">
                    <!-- Row 1: Name & Age -->
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                        <div class="md:col-span-2">
                            <label class="block text-xs font-medium text-slate-400 mb-1.5">Patient Full Name</label>
                            <input type="text" id="patientName" required placeholder="e.g., Ali Raza" 
                                class="w-full bg-slate-900/60 border border-slate-700 rounded-xl px-4 py-2.5 text-sm focus:outline-none focus:border-sky-400">
                        </div>
                        <div>
                            <label class="block text-xs font-medium text-slate-400 mb-1.5">Age</label>
                            <input type="number" id="age" value="24" min="1" max="120" required
                                class="w-full bg-slate-900/60 border border-slate-700 rounded-xl px-4 py-2.5 text-sm focus:outline-none focus:border-sky-400">
                        </div>
                    </div>

                    <!-- Row 2: Gender & Skin Type -->
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div>
                            <label class="block text-xs font-medium text-slate-400 mb-1.5">Gender</label>
                            <select id="gender" class="w-full bg-slate-900/60 border border-slate-700 rounded-xl px-4 py-2.5 text-sm focus:outline-none focus:border-sky-400">
                                <option>Male</option>
                                <option>Female</option>
                                <option>Other</option>
                            </select>
                        </div>
                        <div>
                            <label class="block text-xs font-medium text-slate-400 mb-1.5">Skin Type</label>
                            <select id="skinType" class="w-full bg-slate-900/60 border border-slate-700 rounded-xl px-4 py-2.5 text-sm focus:outline-none focus:border-sky-400">
                                <option>Oily</option>
                                <option>Dry</option>
                                <option>Combination</option>
                                <option>Sensitive</option>
                                <option>Normal</option>
                            </select>
                        </div>
                    </div>

                    <!-- Row 3: Interactive Sliders -->
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 pt-2">
                        <div class="bg-slate-900/40 p-4 rounded-2xl border border-slate-800">
                            <div class="flex justify-between text-xs mb-2">
                                <span class="text-slate-400"><i class="fa-solid fa-droplet text-sky-400 mr-1"></i> Daily Water Intake</span>
                                <span class="font-bold text-sky-400"><span id="waterVal">6</span> Glasses</span>
                            </div>
                            <input type="range" id="waterIntake" min="1" max="15" value="6" oninput="document.getElementById('waterVal').innerText = this.value"
                                class="w-full accent-sky-400 cursor-pointer">
                        </div>

                        <div class="bg-slate-900/40 p-4 rounded-2xl border border-slate-800">
                            <div class="flex justify-between text-xs mb-2">
                                <span class="text-slate-400"><i class="fa-solid fa-moon text-indigo-400 mr-1"></i> Sleep Duration</span>
                                <span class="font-bold text-indigo-400"><span id="sleepVal">7</span> Hours</span>
                            </div>
                            <input type="range" id="sleepHours" min="3" max="12" value="7" oninput="document.getElementById('sleepVal').innerText = this.value"
                                class="w-full accent-indigo-400 cursor-pointer">
                        </div>
                    </div>

                    <!-- Row 4: Stress & Diet -->
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div>
                            <label class="block text-xs font-medium text-slate-400 mb-1.5">Stress Level</label>
                            <select id="stressLevel" class="w-full bg-slate-900/60 border border-slate-700 rounded-xl px-4 py-2.5 text-sm focus:outline-none focus:border-sky-400">
                                <option>Low</option>
                                <option>Moderate</option>
                                <option>High</option>
                            </select>
                        </div>
                        <div>
                            <label class="block text-xs font-medium text-slate-400 mb-1.5">Diet Quality</label>
                            <select id="dietQuality" class="w-full bg-slate-900/60 border border-slate-700 rounded-xl px-4 py-2.5 text-sm focus:outline-none focus:border-sky-400">
                                <option>Healthy</option>
                                <option>Balanced</option>
                                <option>Processed / Junk</option>
                            </select>
                        </div>
                    </div>

                    <!-- Submit Button -->
                    <button type="submit" class="w-full py-3.5 px-6 rounded-xl bg-gradient-to-r from-sky-500 to-indigo-600 hover:from-sky-400 hover:to-indigo-500 text-white font-semibold shadow-lg shadow-sky-500/25 transition-all flex items-center justify-center gap-2 cursor-pointer mt-4">
                        <i class="fa-solid fa-wand-magic-sparkles"></i> Generate Full Skin Health Report
                    </button>
                </form>
            </div>
        </div>
    </main>

    <!-- Dynamic Report Result Section (Hidden by default) -->
    <section id="reportSection" class="max-w-6xl mx-auto mt-8 hidden">
        <div class="glass-card rounded-3xl p-6 md:p-8 border-t-4 border-sky-400">
            <div class="flex flex-wrap justify-between items-center gap-4 border-b border-slate-700/60 pb-4 mb-6">
                <div>
                    <span class="text-xs uppercase tracking-wider text-sky-400 font-semibold">Diagnostic Summary</span>
                    <h3 class="text-xl font-bold" id="reportTitle">Patient Analysis Report</h3>
                </div>
                <button onclick="window.print()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-medium border border-slate-600">
                    <i class="fa-solid fa-print mr-1.5"></i> Print / Save PDF
                </button>
