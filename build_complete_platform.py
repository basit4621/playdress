import sys
import os

sys.path.append('/home/gamp/.gemini/antigravity/scratch/play-dress-up-web')
from assets_b64 import (
    MODEL_HER_FASHION, MODEL_EMERALD, MODEL_NOIR, MODEL_ROSE, DOLL_2D,
    PROD_TOP, PROD_SKIRT, PROD_BOOTS, PROD_BAG, PROD_EMERALD, PROD_NOIR, PROD_ROSE
)

html_code = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PLAY DRESS UP – Modest Fashion & Digital Twin Platform</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,400&display=swap');
    
    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: #F8F9FA;
    }}
    .font-serif {{
      font-family: 'Playfair Display', serif;
    }}
    
    /* View Switching Animation */
    .view-section {{
      display: none;
      opacity: 0;
      transition: opacity 0.25s ease-in-out;
    }}
    .view-section.active {{
      display: block;
      opacity: 1;
    }}

    /* Nav buttons active styling */
    .nav-btn.active {{
      background-color: #1c1917;
      color: #ffffff !important;
    }}

    /* Interactive Card Selected Style */
    .store-card {{
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    .card-active-equipped {{
      border-color: #1c1917 !important;
      background-color: #FAFAFA !important;
      box-shadow: 0 8px 20px -4px rgba(0, 0, 0, 0.08);
    }}

    /* 360 Ring animation */
    @keyframes spin-pedestal {{
      from {{ transform: rotateX(65deg) rotateZ(0deg); }}
      to {{ transform: rotateX(65deg) rotateZ(360deg); }}
    }}
    .animate-spin-pedestal {{
      animation: spin-pedestal 20s linear infinite;
    }}

    /* Sliders styling */
    input[type=range] {{
      accent-color: #e11d48;
    }}
  </style>
</head>
<body class="text-stone-800 antialiased min-h-screen flex flex-col selection:bg-rose-100 selection:text-rose-900">

  <!-- ======================================================== -->
  <!-- TOP PERSISTENT NAVIGATION BAR                           -->
  <!-- ======================================================== -->
  <header class="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-stone-200 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between">
      
      <!-- Brand Logo -->
      <div class="flex items-center space-x-3 cursor-pointer" onclick="navigateTo('view-home')">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-rose-500 via-pink-600 to-amber-400 flex items-center justify-center text-white font-serif font-extrabold text-xl shadow-md shadow-rose-200">
          P
        </div>
        <div>
          <span class="text-lg font-bold font-serif tracking-tight text-stone-900">PLAY DRESS UP</span>
          <span class="block text-[10px] font-bold tracking-widest text-rose-600 uppercase -mt-0.5">Fashion Tech & Dressing Room</span>
        </div>
      </div>

      <!-- Main Navigation Menu -->
      <nav class="hidden md:flex items-center space-x-1 text-xs font-bold text-stone-600">
        <button onclick="navigateTo('view-home')" id="nav-btn-home" class="nav-btn active px-3.5 py-2 rounded-xl hover:text-stone-900 hover:bg-stone-100 transition" data-target="view-home">
          🏠 Home
        </button>
        <button onclick="navigateTo('view-avatar')" id="nav-btn-avatar" class="nav-btn px-3.5 py-2 rounded-xl hover:text-stone-900 hover:bg-stone-100 transition" data-target="view-avatar">
          🪞 My Avatar & Body
        </button>
        <button onclick="navigateTo('view-studio')" id="nav-btn-studio" class="nav-btn px-3.5 py-2 rounded-xl hover:text-stone-900 hover:bg-stone-100 transition" data-target="view-studio">
          👗 Unified Dressing Room & Store
        </button>
        <button onclick="navigateTo('view-challenges')" id="nav-btn-challenges" class="nav-btn px-3.5 py-2 rounded-xl hover:text-stone-900 hover:bg-stone-100 transition" data-target="view-challenges">
          🏆 Daily Challenges
        </button>
        <button onclick="navigateTo('view-profile')" id="nav-btn-profile" class="nav-btn px-3.5 py-2 rounded-xl hover:text-stone-900 hover:bg-stone-100 transition" data-target="view-profile">
          🛍️ My Wardrobe (<span id="nav-saved-count">2</span>)
        </button>
      </nav>

      <!-- Right Controls: Coins & Profile -->
      <div class="flex items-center space-x-3">
        <!-- Coin Reward Balance -->
        <div class="flex items-center space-x-1.5 bg-amber-50 border border-amber-200/90 px-3.5 py-1.5 rounded-full text-amber-900 text-xs font-bold shadow-sm cursor-pointer" onclick="navigateTo('view-challenges')" title="Spend in store or earn more in challenges!">
          <span>🪙</span>
          <span id="user-coins-display">450</span>
          <span class="text-[10px] text-amber-700 font-medium hidden sm:inline">Coins ($15 Off)</span>
        </div>

        <!-- User Profile Pill -->
        <div onclick="navigateTo('view-profile')" class="cursor-pointer flex items-center space-x-2 border-l border-stone-200 pl-3">
          <div class="w-8 h-8 rounded-full bg-stone-900 text-white flex items-center justify-center font-bold text-xs ring-2 ring-rose-200">
            O
          </div>
          <span class="text-xs font-bold text-stone-700 hidden lg:inline">Oreoluwa</span>
        </div>
      </div>

    </div>
  </header>

  <!-- NOTIFICATION TOAST -->
  <div id="app-toast" class="fixed bottom-5 right-5 z-50 transform translate-y-24 opacity-0 transition-all duration-300 bg-stone-900 text-white px-5 py-3 rounded-2xl shadow-xl flex items-center gap-3 text-xs font-semibold border border-stone-700">
    <span id="toast-icon">✨</span>
    <span id="toast-msg">Notification message</span>
  </div>

  <!-- MAIN BODY -->
  <main class="flex-1 max-w-7xl w-full mx-auto p-3 sm:p-5 md:p-6 lg:p-8">

    <!-- ======================================================== -->
    <!-- VIEW 1: HOME & DISCOVERY PAGE                            -->
    <!-- ======================================================== -->
    <section id="view-home" class="view-section active space-y-8">
      
      <!-- Hero Banner -->
      <div class="relative overflow-hidden rounded-[36px] bg-gradient-to-r from-stone-900 via-stone-800 to-rose-950 text-white p-8 sm:p-12 shadow-2xl">
        <div class="relative z-10 max-w-2xl">
          <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/10 backdrop-blur-md text-[11px] font-bold uppercase tracking-wider mb-4 border border-white/20">
            ✨ Welcome to Play Dress Up
          </span>
          <h1 class="text-3xl sm:text-5xl font-extrabold font-serif leading-tight">
            Style in the Dressing Room.<br><span class="text-rose-300">Delivered to Your Doorstep.</span>
          </h1>
          <p class="mt-4 text-sm sm:text-base text-stone-300 leading-relaxed">
            Create a photorealistic avatar matching your exact measurements. Mix and match multi-vendor designer collections, unlock coin discounts from daily challenges, and order full outfits with guaranteed doorstep delivery.
          </p>

          <div class="mt-7 flex flex-wrap gap-3">
            <button onclick="navigateTo('view-studio')" class="px-6 py-3.5 rounded-2xl bg-white text-stone-900 font-extrabold text-xs shadow-lg hover:bg-stone-100 transition flex items-center gap-2">
              <span>Open Unified Dressing Room & Store</span>
              <span>→</span>
            </button>
            <button onclick="navigateTo('view-avatar')" class="px-6 py-3.5 rounded-2xl bg-white/10 backdrop-blur-md hover:bg-white/20 text-white font-bold text-xs transition border border-white/20">
              Customize Body Avatar
            </button>
            <button onclick="navigateTo('view-challenges')" class="px-6 py-3.5 rounded-2xl bg-amber-500/20 hover:bg-amber-500/30 text-amber-200 font-bold text-xs transition border border-amber-400/30">
              🪙 Earn Styling Coins
            </button>
          </div>
        </div>

        <div class="absolute -right-10 -bottom-10 w-96 h-96 rounded-full bg-rose-500/10 blur-3xl pointer-events-none"></div>
      </div>

      <!-- Quick Category Shortcuts -->
      <div>
        <div class="flex items-center justify-between mb-4">
          <div>
            <h2 class="text-xl font-bold font-serif text-stone-900">Featured Collections</h2>
            <p class="text-xs text-stone-500">Tap any collection to try it immediately on your avatar</p>
          </div>
          <button onclick="navigateTo('view-studio')" class="text-xs font-bold text-rose-600 hover:underline">
            View All in Dressing Room →
          </button>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-4 gap-4">
          <div onclick="navigateTo('view-studio'); selectOutfitLook('minimalist');" class="cursor-pointer group p-5 bg-white rounded-3xl border border-stone-200 hover:border-stone-900 shadow-sm hover:shadow-md transition text-center">
            <div class="w-14 h-14 mx-auto rounded-2xl bg-stone-100 text-3xl flex items-center justify-center group-hover:scale-110 transition">✨</div>
            <h3 class="font-bold text-stone-900 text-xs mt-3">Neutral Luxe</h3>
            <p class="text-[11px] text-stone-500 mt-0.5">Top + Skirt + Boots + Bag</p>
            <span class="inline-block mt-2 text-[10px] font-bold text-stone-900 bg-stone-100 px-2 py-0.5 rounded">HER FASHION</span>
          </div>

          <div onclick="navigateTo('view-studio'); selectOutfitLook('emerald');" class="cursor-pointer group p-5 bg-white rounded-3xl border border-stone-200 hover:border-emerald-600 shadow-sm hover:shadow-md transition text-center">
            <div class="w-14 h-14 mx-auto rounded-2xl bg-emerald-50 text-3xl flex items-center justify-center group-hover:scale-110 transition">💚</div>
            <h3 class="font-bold text-stone-900 text-xs mt-3">Emerald Silk Maxi</h3>
            <p class="text-[11px] text-stone-500 mt-0.5">Silk Wrap Evening Dress</p>
            <span class="inline-block mt-2 text-[10px] font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded">ZARA Collection</span>
          </div>

          <div onclick="navigateTo('view-studio'); selectOutfitLook('noir');" class="cursor-pointer group p-5 bg-white rounded-3xl border border-stone-200 hover:border-stone-900 shadow-sm hover:shadow-md transition text-center">
            <div class="w-14 h-14 mx-auto rounded-2xl bg-stone-100 text-3xl flex items-center justify-center group-hover:scale-110 transition">🖤</div>
            <h3 class="font-bold text-stone-900 text-xs mt-3">Velvet Noir</h3>
            <p class="text-[11px] text-stone-500 mt-0.5">Midnight Velvet Gown</p>
            <span class="inline-block mt-2 text-[10px] font-bold text-stone-800 bg-stone-100 px-2 py-0.5 rounded">MANGO Studio</span>
          </div>

          <div onclick="navigateTo('view-studio'); selectOutfitLook('rose');" class="cursor-pointer group p-5 bg-white rounded-3xl border border-stone-200 hover:border-rose-400 shadow-sm hover:shadow-md transition text-center">
            <div class="w-14 h-14 mx-auto rounded-2xl bg-rose-50 text-3xl flex items-center justify-center group-hover:scale-110 transition">🌸</div>
            <h3 class="font-bold text-stone-900 text-xs mt-3">Rose Quartz</h3>
            <p class="text-[11px] text-stone-500 mt-0.5">Blush Satin Wrap Gown</p>
            <span class="inline-block mt-2 text-[10px] font-bold text-rose-600 bg-rose-50 px-2 py-0.5 rounded">H&M Premium</span>
          </div>
        </div>
      </div>

      <!-- Feature Highlights -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
        <div class="p-6 bg-white rounded-3xl border border-stone-200 shadow-sm">
          <div class="text-2xl mb-2">🪞</div>
          <h3 class="font-bold text-sm text-stone-900">Photorealistic Body Twin</h3>
          <p class="text-xs text-stone-500 mt-1 leading-relaxed">
            Customize bust, waist, and build sliders. The garments drape accurately on your proportions.
          </p>
        </div>

        <div class="p-6 bg-white rounded-3xl border border-stone-200 shadow-sm">
          <div class="text-2xl mb-2">🪙</div>
          <h3 class="font-bold text-sm text-stone-900">Play, Style & Earn Discounts</h3>
          <p class="text-xs text-stone-500 mt-1 leading-relaxed">
            Earn coins by joining daily styling challenges and referring friends. 100% redeemable on real clothes.
          </p>
        </div>

        <div class="p-6 bg-white rounded-3xl border border-stone-200 shadow-sm">
          <div class="text-2xl mb-2">📦</div>
          <h3 class="font-bold text-sm text-stone-900">Doorstep Delivery Guarantee</h3>
          <p class="text-xs text-stone-500 mt-1 leading-relaxed">
            Order complete outfits straight from the dressing room. Shipped directly to your home with 30-day returns.
          </p>
        </div>
      </div>

    </section>

    <!-- ======================================================== -->
    <!-- VIEW 2: AVATAR CUSTOMIZER & MEASUREMENTS (PAGE 2)         -->
    <!-- ======================================================== -->
    <section id="view-avatar" class="view-section space-y-6">
      
      <!-- Top Title -->
      <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-4 border-b border-stone-200 gap-4">
        <div>
          <span class="text-[10px] font-extrabold uppercase tracking-wider text-rose-600">Avatar Engine</span>
          <h1 class="text-2xl sm:text-3xl font-extrabold font-serif text-stone-900">Customize Your Digital Twin</h1>
          <p class="text-xs text-stone-500">Fine-tune your bust, waist, shoulders, and complexion. Changes persist in your profile.</p>
        </div>
        <button onclick="saveAvatarAndGoStudio()" class="px-6 py-2.5 rounded-2xl bg-stone-900 hover:bg-black text-white font-bold text-xs shadow transition flex items-center gap-2">
          <span>Save & Go To Dressing Room</span>
          <span>→</span>
        </button>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
        
        <!-- LEFT: Live Avatar Canvas (100% Clean Cutout Doll) -->
        <div class="lg:col-span-5 bg-gradient-to-b from-stone-100 to-white p-6 rounded-3xl border border-stone-200 flex flex-col items-center justify-center relative shadow-sm min-h-[500px]">
          <div class="absolute top-4 left-4 bg-white/90 backdrop-blur-sm px-3 py-1 rounded-full text-[10px] font-bold text-stone-600 border border-stone-200">
            Real-Time Avatar Canvas
          </div>

          <!-- Clean Doll Avatar Image (No Background) -->
          <div class="relative w-64 h-[440px] flex items-center justify-center">
            <img id="customizer-doll-preview" src="{DOLL_2D}" alt="Doll Avatar" class="h-full object-contain drop-shadow-xl select-none transition-transform duration-300">
          </div>

          <!-- Bottom Summary Pill -->
          <div class="mt-2 bg-white px-4 py-1.5 rounded-full border border-stone-200 text-xs font-bold text-stone-700 shadow-sm">
            <span>Bust: <strong id="lbl-bust">34"</strong></span> • 
            <span>Waist: <strong id="lbl-waist">26"</strong></span> • 
            <span>Build: <strong id="lbl-build">Hourglass</strong></span>
          </div>
        </div>

        <!-- RIGHT: Measurement Sliders & Options (Inspired by inspo_2) -->
        <div class="lg:col-span-7 space-y-4">
          
          <!-- 1. Measurement Sliders -->
          <div class="bg-white p-5 rounded-3xl border border-stone-200 shadow-sm space-y-4">
            <h3 class="text-xs font-extrabold text-stone-800 uppercase tracking-wider">1. Body Measurements (Inches)</h3>
            
            <!-- Bust Slider -->
            <div>
              <div class="flex justify-between text-xs font-bold text-stone-700 mb-1.5">
                <span>Bust Size</span>
                <span id="val-bust">34 in</span>
              </div>
              <input type="range" min="30" max="46" value="34" class="w-full h-2 bg-stone-100 rounded-lg cursor-pointer" oninput="updateMeasure('bust', this.value)">
            </div>

            <!-- Waist Slider -->
            <div>
              <div class="flex justify-between text-xs font-bold text-stone-700 mb-1.5">
                <span>Waist Size</span>
                <span id="val-waist">26 in</span>
              </div>
              <input type="range" min="22" max="42" value="26" class="w-full h-2 bg-stone-100 rounded-lg cursor-pointer" oninput="updateMeasure('waist', this.value)">
            </div>

            <!-- Shoulders Slider -->
            <div>
              <div class="flex justify-between text-xs font-bold text-stone-700 mb-1.5">
                <span>Shoulder Width</span>
                <span id="val-shoulders">15 in</span>
              </div>
              <input type="range" min="12" max="22" value="15" class="w-full h-2 bg-stone-100 rounded-lg cursor-pointer" oninput="updateMeasure('shoulders', this.value)">
            </div>
          </div>

          <!-- 2. Body Shape Buttons -->
          <div class="bg-white p-5 rounded-3xl border border-stone-200 shadow-sm">
            <h3 class="text-xs font-extrabold text-stone-800 uppercase tracking-wider mb-3">2. Body Silhouette</h3>
            <div class="grid grid-cols-3 sm:grid-cols-5 gap-2">
              <button onclick="setBodySilhouette('Hourglass')" class="sil-btn active p-3 rounded-2xl border-2 border-stone-900 bg-stone-50 text-center text-xs font-bold text-stone-900 transition flex flex-col items-center gap-1">
                <span>⏳</span>
                <span>Hourglass</span>
              </button>
              <button onclick="setBodySilhouette('Pear / Curvy')" class="sil-btn p-3 rounded-2xl border border-stone-200 hover:border-stone-900 text-center text-xs font-bold text-stone-700 transition flex flex-col items-center gap-1">
                <span>🍐</span>
                <span>Curvy</span>
              </button>
              <button onclick="setBodySilhouette('Petite / Slim')" class="sil-btn p-3 rounded-2xl border border-stone-200 hover:border-stone-900 text-center text-xs font-bold text-stone-700 transition flex flex-col items-center gap-1">
                <span>🧍🏽‍♀️</span>
                <span>Petite</span>
              </button>
              <button onclick="setBodySilhouette('Plus-Size')" class="sil-btn p-3 rounded-2xl border border-stone-200 hover:border-stone-900 text-center text-xs font-bold text-stone-700 transition flex flex-col items-center gap-1">
                <span>🌸</span>
                <span>Plus</span>
              </button>
              <button onclick="setBodySilhouette('Athletic')" class="sil-btn p-3 rounded-2xl border border-stone-200 hover:border-stone-900 text-center text-xs font-bold text-stone-700 transition flex flex-col items-center gap-1">
                <span>💪🏽</span>
                <span>Athletic</span>
              </button>
            </div>
          </div>

          <!-- 3. Skin Tone Palette -->
          <div class="bg-white p-5 rounded-3xl border border-stone-200 shadow-sm">
            <h3 class="text-xs font-extrabold text-stone-800 uppercase tracking-wider mb-3">3. Skin Complexion</h3>
            <div class="flex items-center gap-3">
              <button onclick="selectComplexion('Deep Ebony', '#402312')" class="w-10 h-10 rounded-full border-2 border-white ring-2 ring-stone-200 hover:scale-110 transition shadow-sm" style="background-color: #402312;"></button>
              <button onclick="selectComplexion('Rich Cocoa', '#6B4021')" class="w-10 h-10 rounded-full border-2 border-white ring-2 ring-stone-900 scale-110 transition shadow-sm" style="background-color: #6B4021;"></button>
              <button onclick="selectComplexion('Caramel Glow', '#A0683A')" class="w-10 h-10 rounded-full border-2 border-white ring-2 ring-stone-200 hover:scale-110 transition shadow-sm" style="background-color: #A0683A;"></button>
              <button onclick="selectComplexion('Warm Honey', '#C8935C')" class="w-10 h-10 rounded-full border-2 border-white ring-2 ring-stone-200 hover:scale-110 transition shadow-sm" style="background-color: #C8935C;"></button>
              <button onclick="selectComplexion('Golden Ivory', '#ECC097')" class="w-10 h-10 rounded-full border-2 border-white ring-2 ring-stone-200 hover:scale-110 transition shadow-sm" style="background-color: #ECC097;"></button>
            </div>
          </div>

        </div>

      </div>

    </section>

    <!-- ======================================================== -->
    <!-- VIEW 3: UNIFIED DRESSING ROOM & STORE (EXACT HER FASHION) -->
    <!-- ======================================================== -->
    <section id="view-studio" class="view-section space-y-4">

      <!-- Main Studio Box -->
      <div class="bg-[#EDEDED] p-3 sm:p-5 rounded-[36px] shadow-2xl border border-stone-300">

        <!-- Top Controls Bar -->
        <div class="flex flex-wrap items-center justify-between pb-3.5 mb-4 border-b border-stone-300/80 px-1 gap-3">
          
          <div class="flex items-center gap-3">
            <div class="w-9 h-9 rounded-2xl bg-stone-900 text-white flex items-center justify-center font-serif font-extrabold text-lg shadow">
              P
            </div>
            <div>
              <span class="text-base font-extrabold font-serif tracking-tight text-stone-900">UNIFIED DRESSING STUDIO</span>
              <span class="block text-[10px] font-bold text-stone-500">HER FASHION • Multi-Vendor Live Fitting</span>
            </div>
          </div>

          <!-- Avatar Mode Switcher: 3D Runway Model vs 2D Doll Avatar -->
          <div class="bg-white/90 backdrop-blur p-1 rounded-2xl border border-stone-200 flex items-center gap-1 shadow-sm">
            <button onclick="setAvatarMode('3d')" id="btn-mode-3d" class="px-3 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5 bg-stone-900 text-white shadow-sm">
              <span>👠</span> 3D Runway Model
            </button>
            <button onclick="setAvatarMode('2d')" id="btn-mode-2d" class="px-3 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5 text-stone-600 hover:text-stone-900">
              <span>🪞</span> 2D Doll Avatar
            </button>
          </div>

          <!-- Action Buttons -->
          <div class="flex items-center gap-2">
            <button onclick="saveCurrentLookToWardrobe()" class="px-4 py-2 rounded-xl bg-white hover:bg-stone-50 border border-stone-300 text-stone-700 text-xs font-bold transition flex items-center gap-1 shadow-sm">
              <span>💾 Save Look</span>
            </button>
            <button onclick="navigateTo('view-challenges')" class="px-4 py-2 rounded-xl bg-amber-500 hover:bg-amber-600 text-white text-xs font-bold transition flex items-center gap-1 shadow-sm">
              <span>🏆 Enter Challenge</span>
            </button>
          </div>

        </div>

        <!-- 3-COLUMN UNIFIED GRID: Left Store | Center Avatar | Right Summary -->
        <div class="grid grid-cols-1 lg:grid-cols-10 gap-4 md:gap-5 items-stretch">

          <!-- ======================================================== -->
          <!-- COLUMN 1 (LEFT, 4 cols): STORE CATALOG (HER FASHION)     -->
          <!-- ======================================================== -->
          <div class="lg:col-span-4 bg-white p-4 sm:p-5 rounded-[32px] shadow-sm border border-stone-200 flex flex-col justify-between">
            
            <div>
              <!-- Store Brand & Switcher -->
              <div class="flex items-center justify-between pb-3 border-b border-stone-100 mb-3.5">
                <div>
                  <span class="text-[10px] font-bold text-stone-400 uppercase tracking-widest block">Shop by Store</span>
                  <div class="flex items-center gap-1.5 cursor-pointer group">
                    <h2 id="store-brand-title" class="text-base font-extrabold text-stone-900 font-serif tracking-tight">HER FASHION</h2>
                    <span class="text-xs text-stone-400 group-hover:text-stone-800 transition">▾</span>
                  </div>
                </div>
                
                <span class="inline-flex items-center gap-1 bg-emerald-50 text-emerald-700 border border-emerald-200 text-[10px] font-bold px-2 py-0.5 rounded-full">
                  <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span> In Stock
                </span>
              </div>

              <!-- Search Bar -->
              <div class="relative mb-3.5">
                <span class="absolute inset-y-0 left-3 flex items-center text-stone-400 text-xs">🔍</span>
                <input type="text" placeholder="Search dresses, tops, boots, bags..." class="w-full pl-8 pr-3 py-2 bg-stone-50 border border-stone-200 rounded-xl text-xs font-medium text-stone-800 focus:bg-white focus:outline-none focus:ring-1 focus:ring-stone-400 transition placeholder:text-stone-400">
              </div>

              <!-- Curated Complete Looks (Tap to Change Avatar Outfit) -->
              <div class="mb-3.5">
                <span class="text-[10px] font-extrabold text-stone-400 uppercase tracking-wider block mb-1.5">Curated Complete Looks (Tap to Style Avatar)</span>
                <div class="grid grid-cols-2 gap-1.5">
                  <button onclick="selectOutfitLook('minimalist')" id="btn-look-minimalist" class="look-btn p-2 rounded-xl text-left border border-stone-900 bg-stone-900 text-white text-[11px] font-bold transition flex items-center justify-between">
                    <span>✨ Look 1: Neutral Luxe</span>
                    <span class="text-[9px] opacity-75">$558</span>
                  </button>
                  <button onclick="selectOutfitLook('emerald')" id="btn-look-emerald" class="look-btn p-2 rounded-xl text-left border border-stone-200 bg-stone-50 hover:bg-emerald-50 text-stone-800 text-[11px] font-bold transition flex items-center justify-between">
                    <span>💚 Look 2: Emerald Silk</span>
                    <span class="text-[9px] text-emerald-700">$89</span>
                  </button>
                  <button onclick="selectOutfitLook('noir')" id="btn-look-noir" class="look-btn p-2 rounded-xl text-left border border-stone-200 bg-stone-50 hover:bg-stone-100 text-stone-800 text-[11px] font-bold transition flex items-center justify-between">
                    <span>🖤 Look 3: Velvet Noir</span>
                    <span class="text-[9px] text-stone-600">$119</span>
                  </button>
                  <button onclick="selectOutfitLook('rose')" id="btn-look-rose" class="look-btn p-2 rounded-xl text-left border border-stone-200 bg-stone-50 hover:bg-rose-50 text-stone-800 text-[11px] font-bold transition flex items-center justify-between">
                    <span>🌸 Look 4: Rose Satin</span>
                    <span class="text-[9px] text-rose-600">$79</span>
                  </button>
                </div>
              </div>

              <!-- Category Filter Pills -->
              <div class="flex items-center gap-1.5 overflow-x-auto pb-1 mb-3.5 text-[11px] font-semibold text-stone-600 scrollbar-none">
                <button onclick="filterCategory('all')" class="cat-pill px-3 py-1 bg-stone-900 text-white rounded-full font-bold">All</button>
                <button onclick="filterCategory('tops')" class="cat-pill px-3 py-1 bg-stone-100 hover:bg-stone-200 text-stone-700 rounded-full transition">Tops</button>
                <button onclick="filterCategory('skirts')" class="cat-pill px-3 py-1 bg-stone-100 hover:bg-stone-200 text-stone-700 rounded-full transition">Skirts</button>
                <button onclick="filterCategory('dresses')" class="cat-pill px-3 py-1 bg-stone-100 hover:bg-stone-200 text-stone-700 rounded-full transition">Dresses</button>
                <button onclick="filterCategory('shoes')" class="cat-pill px-3 py-1 bg-stone-100 hover:bg-stone-200 text-stone-700 rounded-full transition">Shoes</button>
                <button onclick="filterCategory('bags')" class="cat-pill px-3 py-1 bg-stone-100 hover:bg-stone-200 text-stone-700 rounded-full transition">Bags</button>
              </div>

              <!-- 2-COLUMN PRODUCT GRID (EXACT TO HER FASHION) -->
              <div class="grid grid-cols-2 gap-3 max-h-[380px] overflow-y-auto pr-1">

                <!-- Card 1: Off-Shoulder Top -->
                <div onclick="toggleSingleItem('top')" id="card-top" class="store-card card-active-equipped cursor-pointer p-3 rounded-2xl border border-stone-200 hover:border-stone-400 bg-white relative flex flex-col justify-between group">
                  <button onclick="event.stopPropagation(); toggleFav(this)" class="absolute top-2.5 right-2.5 text-stone-300 hover:text-red-500 text-xs transition">♡</button>
                  <div class="w-full h-24 bg-[#F8F8F8] rounded-xl flex items-center justify-center p-2 mb-2 group-hover:scale-105 transition">
                    <img src="{PROD_TOP}" alt="Off-shoulder Top" class="h-full object-contain">
                  </div>
                  <div>
                    <span class="text-[9px] font-bold text-stone-400 uppercase tracking-wider">ZARA</span>
                    <h4 class="text-xs font-bold text-stone-900 leading-tight">Off-shoulder top</h4>
                    <div class="flex items-center justify-between mt-1">
                      <span class="text-xs font-extrabold text-stone-900">$29.90</span>
                      <span id="badge-top" class="text-[9px] bg-stone-900 text-white font-bold px-1.5 py-0.5 rounded">Equipped ✓</span>
                    </div>
                  </div>
                </div>

                <!-- Card 2: Pleated Maxi Skirt -->
                <div onclick="toggleSingleItem('skirt')" id="card-skirt" class="store-card card-active-equipped cursor-pointer p-3 rounded-2xl border border-stone-200 hover:border-stone-400 bg-white relative flex flex-col justify-between group">
                  <button onclick="event.stopPropagation(); toggleFav(this)" class="absolute top-2.5 right-2.5 text-stone-300 hover:text-red-500 text-xs transition">♡</button>
                  <div class="w-full h-24 bg-[#F8F8F8] rounded-xl flex items-center justify-center p-2 mb-2 group-hover:scale-105 transition">
                    <img src="{PROD_SKIRT}" alt="Pleated Maxi Skirt" class="h-full object-contain">
                  </div>
                  <div>
                    <span class="text-[9px] font-bold text-stone-400 uppercase tracking-wider">MANGO</span>
                    <h4 class="text-xs font-bold text-stone-900 leading-tight">Pleated maxi skirt</h4>
                    <div class="flex items-center justify-between mt-1">
                      <span class="text-xs font-extrabold text-stone-900">$49.99</span>
                      <span id="badge-skirt" class="text-[9px] bg-stone-900 text-white font-bold px-1.5 py-0.5 rounded">Equipped ✓</span>
                    </div>
                  </div>
                </div>

                <!-- Card 3: Knee-High Leather Boots -->
                <div onclick="toggleSingleItem('boots')" id="card-boots" class="store-card card-active-equipped cursor-pointer p-3 rounded-2xl border border-stone-200 hover:border-stone-400 bg-white relative flex flex-col justify-between group">
                  <button onclick="event.stopPropagation(); toggleFav(this)" class="absolute top-2.5 right-2.5 text-stone-300 hover:text-red-500 text-xs transition">♡</button>
                  <div class="w-full h-24 bg-[#F8F8F8] rounded-xl flex items-center justify-center p-2 mb-2 group-hover:scale-105 transition">
                    <img src="{PROD_BOOTS}" alt="Leather Boots" class="h-full object-contain">
                  </div>
                  <div>
                    <span class="text-[9px] font-bold text-stone-400 uppercase tracking-wider">BERSHKA</span>
                    <h4 class="text-xs font-bold text-stone-900 leading-tight">Knee-high leather boots</h4>
                    <div class="flex items-center justify-between mt-1">
                      <span class="text-xs font-extrabold text-stone-900">$129.00</span>
                      <span id="badge-boots" class="text-[9px] bg-stone-900 text-white font-bold px-1.5 py-0.5 rounded">Equipped ✓</span>
                    </div>
                  </div>
                </div>

                <!-- Card 4: Tabby Shoulder Bag -->
                <div onclick="toggleSingleItem('bag')" id="card-bag" class="store-card card-active-equipped cursor-pointer p-3 rounded-2xl border border-stone-200 hover:border-stone-400 bg-white relative flex flex-col justify-between group">
                  <button onclick="event.stopPropagation(); toggleFav(this)" class="absolute top-2.5 right-2.5 text-stone-300 hover:text-red-500 text-xs transition">♡</button>
                  <div class="w-full h-24 bg-[#F8F8F8] rounded-xl flex items-center justify-center p-2 mb-2 group-hover:scale-105 transition">
                    <img src="{PROD_BAG}" alt="Tabby Shoulder Bag" class="h-full object-contain">
                  </div>
                  <div>
                    <span class="text-[9px] font-bold text-stone-400 uppercase tracking-wider">COACH</span>
                    <h4 class="text-xs font-bold text-stone-900 leading-tight">Tabby shoulder bag</h4>
                    <div class="flex items-center justify-between mt-1">
                      <span class="text-xs font-extrabold text-stone-900">$350.00</span>
                      <span id="badge-bag" class="text-[9px] bg-stone-900 text-white font-bold px-1.5 py-0.5 rounded">Equipped ✓</span>
                    </div>
                  </div>
                </div>

                <!-- Card 5: Emerald Silk Wrap Maxi Dress (Direct from User Request!) -->
                <div onclick="selectOutfitLook('emerald')" id="card-emerald" class="store-card cursor-pointer p-3 rounded-2xl border border-stone-200 hover:border-stone-400 bg-white relative flex flex-col justify-between group">
                  <button onclick="event.stopPropagation(); toggleFav(this)" class="absolute top-2.5 right-2.5 text-stone-300 hover:text-red-500 text-xs transition">♡</button>
                  <div class="w-full h-24 bg-emerald-50/50 rounded-xl flex items-center justify-center p-2 mb-2 group-hover:scale-105 transition">
                    <img src="{PROD_EMERALD}" alt="Emerald Silk Wrap Maxi" class="h-full object-contain drop-shadow">
                  </div>
                  <div>
                    <span class="text-[9px] font-bold text-emerald-700 uppercase tracking-wider">ZARA COLLECTION</span>
                    <h4 class="text-xs font-bold text-stone-900 leading-tight">Emerald silk wrap maxi</h4>
                    <div class="flex items-center justify-between mt-1">
                      <span class="text-xs font-extrabold text-stone-900">$89.00</span>
                      <span id="badge-emerald" class="text-[9px] bg-stone-100 text-stone-500 font-bold px-1.5 py-0.5 rounded">Tap to Wear</span>
                    </div>
                  </div>
                </div>

                <!-- Card 6: Velvet Noir Slip Gown -->
                <div onclick="selectOutfitLook('noir')" id="card-noir" class="store-card cursor-pointer p-3 rounded-2xl border border-stone-200 hover:border-stone-400 bg-white relative flex flex-col justify-between group">
                  <button onclick="event.stopPropagation(); toggleFav(this)" class="absolute top-2.5 right-2.5 text-stone-300 hover:text-red-500 text-xs transition">♡</button>
                  <div class="w-full h-24 bg-stone-100/70 rounded-xl flex items-center justify-center p-2 mb-2 group-hover:scale-105 transition">
                    <img src="{PROD_NOIR}" alt="Noir Velvet Gown" class="h-full object-contain drop-shadow">
                  </div>
                  <div>
                    <span class="text-[9px] font-bold text-stone-400 uppercase tracking-wider">MANGO STUDIO</span>
                    <h4 class="text-xs font-bold text-stone-900 leading-tight">Noir velvet slip gown</h4>
                    <div class="flex items-center justify-between mt-1">
                      <span class="text-xs font-extrabold text-stone-900">$119.00</span>
                      <span id="badge-noir" class="text-[9px] bg-stone-100 text-stone-500 font-bold px-1.5 py-0.5 rounded">Tap to Wear</span>
                    </div>
                  </div>
                </div>

              </div>
            </div>

            <!-- Guarantee Footer -->
            <div class="mt-3.5 pt-3 border-t border-stone-100 flex items-center justify-between text-[11px] text-stone-500">
              <span class="flex items-center gap-1.5">
                <span>📦</span> Doorstep delivery in 2-4 days
              </span>
              <span class="font-bold text-stone-700">100% Authentic</span>
            </div>

          </div>

          <!-- ======================================================== -->
          <!-- COLUMN 2 (CENTER, 3 cols): DRESSING ROOM (TRANSPARENT)   -->
          <!-- ======================================================== -->
          <div class="lg:col-span-3 bg-[#E9E9E9] rounded-[32px] p-4 flex flex-col justify-between items-center relative overflow-hidden border border-stone-300 shadow-inner min-h-[580px]">
            
            <!-- Top Status Pill -->
            <div class="w-full flex items-center justify-between z-20">
              <span class="bg-white/90 backdrop-blur-md px-3 py-1 rounded-full text-[10px] font-bold text-stone-700 border border-stone-200/80 shadow-sm flex items-center gap-1.5">
                <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
                <span id="center-tag-text">Look 1 • Neutral Luxe</span>
              </span>

              <span class="bg-stone-900/80 text-white text-[10px] font-bold px-2.5 py-1 rounded-full shadow-sm">
                Live Preview
              </span>
            </div>

            <!-- Left Stack Mini Product Icons (From inspo_3) -->
            <div class="absolute left-4 top-16 z-20 flex flex-col gap-2" id="floating-mini-stack">
              <div class="w-9 h-9 bg-white rounded-xl flex items-center justify-center p-1 shadow-sm border border-stone-200" id="mini-top">
                <img src="{PROD_TOP}" class="h-full object-contain">
              </div>
              <div class="w-9 h-9 bg-white rounded-xl flex items-center justify-center p-1 shadow-sm border border-stone-200" id="mini-skirt">
                <img src="{PROD_SKIRT}" class="h-full object-contain">
              </div>
              <div class="w-9 h-9 bg-white rounded-xl flex items-center justify-center p-1 shadow-sm border border-stone-200" id="mini-boots">
                <img src="{PROD_BOOTS}" class="h-full object-contain">
              </div>
              <div class="w-9 h-9 bg-white rounded-xl flex items-center justify-center p-1 shadow-sm border border-stone-200" id="mini-bag">
                <img src="{PROD_BAG}" class="h-full object-contain">
              </div>
            </div>

            <!-- ===================================================== -->
            <!-- THE MODEL IN THE CENTER (100% TRANSPARENT CUTOUT)     -->
            <!-- ===================================================== -->
            <div class="relative w-full h-[470px] flex flex-col items-center justify-end z-10">
              
              <!-- MODEL CONTAINER -->
              <div class="relative w-[240px] h-[450px] flex items-end justify-center">
                
                <!-- 1. 3D Runway Fashion Model (100% Transparent Cutout) -->
                <img 
                  id="center-model-img" 
                  src="{MODEL_HER_FASHION}" 
                  alt="3D Fashion Model" 
                  class="h-full object-contain select-none drop-shadow-xl z-10 transition-all duration-300"
                  style="display: block;"
                >

                <!-- 2. 2D Doll Avatar (100% Transparent Cutout) -->
                <img 
                  id="center-doll-img" 
                  src="{DOLL_2D}" 
                  alt="2D Doll Avatar" 
                  class="h-full object-contain select-none drop-shadow-xl z-10 transition-all duration-300"
                  style="display: none;"
                >

              </div>

              <!-- 3D CIRCULAR PEDESTAL & 360 RING -->
              <div class="absolute bottom-[-10px] w-[210px] h-[55px] flex items-center justify-center pointer-events-none">
                <div class="w-full h-full bg-gradient-to-b from-stone-100 to-stone-300 rounded-[100%] shadow-lg border border-stone-300/80"></div>
                <div class="absolute w-[80%] h-[75%] bg-gradient-to-b from-white to-stone-200 rounded-[100%] shadow-inner border border-stone-200"></div>
                <div class="absolute w-[95%] h-[90%] border-2 border-dashed border-stone-400/60 rounded-[100%] animate-spin-pedestal flex items-center justify-center"></div>
                <span class="absolute bottom-1 bg-stone-800 text-white text-[9px] font-black px-2 py-0.5 rounded-full shadow-sm z-20">
                  360°
                </span>
              </div>

            </div>

            <!-- Bottom Status Pill -->
            <div class="w-full flex justify-center z-20 mt-1">
              <span class="bg-white/95 backdrop-blur-md px-4 py-1.5 rounded-full border border-stone-200 text-xs font-bold text-stone-800 shadow-sm flex items-center gap-2">
                <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
                <span id="equipped-summary-text">Wearing: Zara Top + Mango Skirt + Leather Boots + Coach Bag</span>
              </span>
            </div>

          </div>

          <!-- ======================================================== -->
          <!-- COLUMN 3 (RIGHT, 3 cols): "YOUR LOOK" SUMMARY            -->
          <!-- ======================================================== -->
          <div class="lg:col-span-3 bg-white p-4 sm:p-5 rounded-[32px] shadow-sm border border-stone-200 flex flex-col justify-between">
            
            <div>
              <!-- Header -->
              <div class="border-b border-stone-100 pb-3 mb-3.5 px-1 flex items-center justify-between">
                <h3 class="text-xs font-extrabold text-stone-800 uppercase tracking-widest">YOUR LOOK</h3>
                <span id="outfit-tag-badge" class="text-[9px] font-extrabold uppercase px-2 py-0.5 bg-stone-100 text-stone-600 rounded-md">Curated Look</span>
              </div>

              <!-- Equipped Items Stack -->
              <div class="space-y-2 mb-4 max-h-[220px] overflow-y-auto pr-1" id="your-look-items-list">
                
                <!-- Item 1: Off-shoulder top -->
                <div id="row-top" class="flex items-center justify-between p-2.5 bg-stone-50 rounded-2xl border border-stone-200/80">
                  <div class="flex items-center gap-2.5">
                    <div class="w-9 h-9 rounded-xl bg-white border border-stone-200 flex items-center justify-center p-1 shadow-sm">
                      <img src="{PROD_TOP}" class="h-full object-contain">
                    </div>
                    <div>
                      <span class="text-[9px] font-bold text-stone-400 uppercase">ZARA</span>
                      <h4 class="text-xs font-bold text-stone-900 leading-tight">Off-shoulder top</h4>
                      <p class="text-xs font-extrabold text-stone-900 mt-0.5">$29.90</p>
                    </div>
                  </div>
                  <span class="text-stone-400 text-xs font-bold">›</span>
                </div>

                <!-- Item 2: Pleated maxi skirt -->
                <div id="row-skirt" class="flex items-center justify-between p-2.5 bg-stone-50 rounded-2xl border border-stone-200/80">
                  <div class="flex items-center gap-2.5">
                    <div class="w-9 h-9 rounded-xl bg-white border border-stone-200 flex items-center justify-center p-1 shadow-sm">
                      <img src="{PROD_SKIRT}" class="h-full object-contain">
                    </div>
                    <div>
                      <span class="text-[9px] font-bold text-stone-400 uppercase">MANGO</span>
                      <h4 class="text-xs font-bold text-stone-900 leading-tight">Pleated maxi skirt</h4>
                      <p class="text-xs font-extrabold text-stone-900 mt-0.5">$49.99</p>
                    </div>
                  </div>
                  <span class="text-stone-400 text-xs font-bold">›</span>
                </div>

                <!-- Item 3: Knee-high leather boots -->
                <div id="row-boots" class="flex items-center justify-between p-2.5 bg-stone-50 rounded-2xl border border-stone-200/80">
                  <div class="flex items-center gap-2.5">
                    <div class="w-9 h-9 rounded-xl bg-white border border-stone-200 flex items-center justify-center p-1 shadow-sm">
                      <img src="{PROD_BOOTS}" class="h-full object-contain">
                    </div>
                    <div>
                      <span class="text-[9px] font-bold text-stone-400 uppercase">BERSHKA</span>
                      <h4 class="text-xs font-bold text-stone-900 leading-tight">Leather boots</h4>
                      <p class="text-xs font-extrabold text-stone-900 mt-0.5">$129.00</p>
                    </div>
                  </div>
                  <span class="text-stone-400 text-xs font-bold">›</span>
                </div>

                <!-- Item 4: Tabby Shoulder Bag -->
                <div id="row-bag" class="flex items-center justify-between p-2.5 bg-stone-50 rounded-2xl border border-stone-200/80">
                  <div class="flex items-center gap-2.5">
                    <div class="w-9 h-9 rounded-xl bg-white border border-stone-200 flex items-center justify-center p-1 shadow-sm">
                      <img src="{PROD_BAG}" class="h-full object-contain">
                    </div>
                    <div>
                      <span class="text-[9px] font-bold text-stone-400 uppercase">COACH</span>
                      <h4 class="text-xs font-bold text-stone-900 leading-tight">Tabby shoulder bag</h4>
                      <p class="text-xs font-extrabold text-stone-900 mt-0.5">$350.00</p>
                    </div>
                  </div>
                  <span class="text-stone-400 text-xs font-bold">›</span>
                </div>

              </div>

              <!-- STYLE & FIT FEEDBACK (HER FASHION inspo_3) -->
              <div class="mb-4 p-3.5 bg-stone-50 rounded-2xl border border-stone-200/80 space-y-2 text-xs text-stone-600">
                <h4 class="text-[10px] font-extrabold uppercase tracking-wider text-stone-500">STYLE & FIT</h4>
                <div class="space-y-1.5 text-[11px]">
                  <p class="flex items-center justify-between font-semibold text-stone-700">
                    <span class="flex items-center gap-1.5">
                      <span class="w-3.5 h-3.5 rounded-full border border-stone-400 flex items-center justify-center text-[9px]">○</span>
                      <span id="fit-size-text">Fits your size (Bust 34", Waist 26")</span>
                    </span>
                    <span class="text-stone-400 text-[10px]">ⓘ</span>
                  </p>
                  <p class="flex items-center justify-between font-semibold text-stone-700">
                    <span class="flex items-center gap-1.5">
                      <span class="w-3.5 h-3.5 rounded-full border border-stone-400 flex items-center justify-center text-[9px]">○</span>
                      <span id="fit-color-text">Color harmony: Warm Taupe & Cream</span>
                    </span>
                    <span class="text-stone-400 text-[10px]">ⓘ</span>
                  </p>
                  <p class="flex items-center justify-between font-semibold text-stone-700">
                    <span class="flex items-center gap-1.5">
                      <span class="w-3.5 h-3.5 rounded-full border border-stone-400 flex items-center justify-center text-[9px]">○</span>
                      <span id="fit-occasion-text">Occasion: Evening Casual</span>
                    </span>
                    <span class="text-stone-400 text-[10px]">ⓘ</span>
                  </p>
                </div>
              </div>

            </div>

            <!-- PRICING & CHECKOUT (COIN VOUCHER APPLIED) -->
            <div class="border-t border-stone-100 pt-3 space-y-2.5">
              
              <div class="space-y-1.5 text-xs text-stone-600">
                <div class="flex items-center justify-between font-medium">
                  <span>Subtotal</span>
                  <span id="subtotal-val" class="font-bold text-stone-800">$558.89</span>
                </div>
                
                <div class="flex items-center justify-between font-medium text-emerald-700 bg-emerald-50 px-2 py-1 rounded-lg">
                  <span class="flex items-center gap-1">
                    <span>🪙</span> Coins Voucher (150 Coins)
                  </span>
                  <span class="font-bold">-$15.00</span>
                </div>
                
                <div class="flex items-center justify-between font-medium text-stone-500">
                  <span>Doorstep Delivery</span>
                  <span class="text-stone-800 font-bold">FREE</span>
                </div>
                
                <div class="flex items-center justify-between text-base font-extrabold text-stone-900 border-t border-stone-200/80 pt-1.5">
                  <span>Total</span>
                  <span id="total-val">$543.89</span>
                </div>
              </div>

              <!-- Checkout Button -->
              <button onclick="openCheckoutModal()" class="w-full py-3 px-4 bg-stone-900 hover:bg-black text-white rounded-2xl font-bold text-xs uppercase tracking-wider shadow-lg hover:shadow-xl transition flex items-center justify-center gap-2 group">
                <span>Shop the Look</span>
                <span class="group-hover:translate-x-0.5 transition">→</span>
              </button>

              <p class="text-[10px] text-center text-stone-400">Secure delivery to your doorstep • 30-day free returns</p>

            </div>

          </div>

        </div>

      </div>

    </section>

    <!-- ======================================================== -->
    <!-- VIEW 4: DAILY CHALLENGES & EARN COINS (PAGE 4)           -->
    <!-- ======================================================== -->
    <section id="view-challenges" class="view-section space-y-8">
      
      <!-- Challenge Banner -->
      <div class="bg-gradient-to-r from-amber-500 via-rose-500 to-pink-600 rounded-3xl p-6 sm:p-8 text-white shadow-xl">
        <div class="max-w-2xl">
          <span class="inline-block px-3 py-1 bg-white/20 backdrop-blur-md rounded-full text-xs font-bold uppercase tracking-wider mb-2">
            🏆 Gamified Styling Arena
          </span>
          <h2 class="text-3xl font-extrabold font-serif">Daily Style Challenges & Coin Rewards</h2>
          <p class="mt-2 text-rose-100 text-sm leading-relaxed">
            Test your styling eye! Compete in themed challenges judged on <strong>Color Harmony, Silhouette Fit, and Theme Accuracy</strong>. Earn real coins you can spend for vouchers in the shop.
          </p>
        </div>
      </div>

      <!-- Challenges List -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        
        <!-- Challenge 1 -->
        <div class="bg-white rounded-3xl border border-stone-200 p-6 flex flex-col justify-between shadow-sm hover:shadow-md transition">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="px-2.5 py-1 rounded-full bg-rose-100 text-rose-700 text-[11px] font-bold uppercase">Active Today</span>
              <span class="text-xs font-bold text-amber-600">🪙 +150 Coins</span>
            </div>
            <h3 class="text-lg font-bold text-stone-900">Sunday Best: Emerald Grace</h3>
            <p class="text-xs text-stone-500 mt-1 leading-relaxed">
              Style an exquisite evening look using emerald silk, gold accents, and elegant proportions.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-stone-100 flex items-center justify-between">
            <span class="text-xs text-stone-400">Ends in 6h 30m</span>
            <button onclick="startChallenge('emerald')" class="px-4 py-2 rounded-xl bg-rose-600 hover:bg-rose-700 text-white font-bold text-xs transition">
              Style for Challenge
            </button>
          </div>
        </div>

        <!-- Challenge 2 -->
        <div class="bg-white rounded-3xl border border-stone-200 p-6 flex flex-col justify-between shadow-sm hover:shadow-md transition">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="px-2.5 py-1 rounded-full bg-stone-100 text-stone-700 text-[11px] font-bold uppercase">Minimalist</span>
              <span class="text-xs font-bold text-amber-600">🪙 +100 Coins</span>
            </div>
            <h3 class="text-lg font-bold text-stone-900">Monday Neutral Luxe</h3>
            <p class="text-xs text-stone-500 mt-1 leading-relaxed">
              Master the art of warm taupe, off-shoulder top, pleated maxi skirt, and tall leather boots.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-stone-100 flex items-center justify-between">
            <span class="text-xs text-stone-400">Ends in 18h</span>
            <button onclick="startChallenge('minimalist')" class="px-4 py-2 rounded-xl bg-stone-900 hover:bg-black text-white font-bold text-xs transition">
              Style for Challenge
            </button>
          </div>
        </div>

        <!-- Challenge 3 -->
        <div class="bg-white rounded-3xl border border-stone-200 p-6 flex flex-col justify-between shadow-sm hover:shadow-md transition">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="px-2.5 py-1 rounded-full bg-pink-100 text-pink-700 text-[11px] font-bold uppercase">Romantic</span>
              <span class="text-xs font-bold text-amber-600">🪙 +120 Coins</span>
            </div>
            <h3 class="text-lg font-bold text-stone-900">Rose Quartz Summer Gala</h3>
            <p class="text-xs text-stone-500 mt-1 leading-relaxed">
              Soft satin blush drape paired with delicate crystal accessories for an outdoor soirée.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t border-stone-100 flex items-center justify-between">
            <span class="text-xs text-stone-400">Starts Tomorrow</span>
            <button onclick="startChallenge('rose')" class="px-4 py-2 rounded-xl bg-amber-500 hover:bg-amber-600 text-white font-bold text-xs transition">
              Preview Look
            </button>
          </div>
        </div>

      </div>

    </section>

    <!-- ======================================================== -->
    <!-- VIEW 5: MY WARDROBE & PROFILE (PAGE 5)                   -->
    <!-- ======================================================== -->
    <section id="view-profile" class="view-section space-y-6">
      
      <div class="bg-white p-6 rounded-3xl border border-stone-200 shadow-sm flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div class="flex items-center space-x-4">
          <div class="w-16 h-16 rounded-2xl bg-gradient-to-tr from-rose-500 to-amber-400 text-white flex items-center justify-center font-bold text-2xl font-serif shadow-md">
            O
          </div>
          <div>
            <h2 class="text-2xl font-bold font-serif text-stone-900">Oreoluwa's Style Profile</h2>
            <p class="text-xs text-stone-500">Stylist Rank: <span class="font-bold text-rose-600">Level 1: Runway Stylist</span> • 🪙 <span class="font-bold text-amber-600">450 Coins</span> Active</p>
          </div>
        </div>
        <button onclick="navigateTo('view-avatar')" class="px-4 py-2 rounded-xl border border-stone-300 hover:bg-stone-50 text-xs font-bold text-stone-700 transition">
          Edit Avatar Measurements
        </button>
      </div>

      <!-- Saved Outfits Section -->
      <div>
        <div class="flex items-center justify-between mb-4">
          <div>
            <h3 class="text-xl font-bold font-serif text-stone-900">My Saved Wardrobe Looks</h3>
            <p class="text-xs text-stone-500">Your custom styled outfits saved from the Dressing Room</p>
          </div>
          <button onclick="navigateTo('view-studio')" class="px-4 py-2 rounded-xl bg-stone-900 hover:bg-black text-white text-xs font-bold transition">
            + Style a New Outfit
          </button>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5" id="saved-outfits-grid">
          
          <!-- Outfit 1 -->
          <div class="bg-white p-4 rounded-3xl border border-stone-200 shadow-sm flex flex-col justify-between">
            <div>
              <div class="h-44 bg-stone-50 rounded-2xl flex items-center justify-center p-2 mb-3">
                <img src="{MODEL_HER_FASHION}" class="h-full object-contain">
              </div>
              <h4 class="font-bold text-sm text-stone-900">HER Fashion: Neutral Luxe</h4>
              <p class="text-xs text-stone-500">4 pieces • Zara Top + Mango Skirt + Boots + Bag</p>
              <p class="text-sm font-extrabold text-stone-900 mt-1">$543.89 <span class="text-[10px] text-emerald-600 font-bold">(Coin voucher applied)</span></p>
            </div>
            <button onclick="navigateTo('view-studio'); selectOutfitLook('minimalist');" class="mt-4 w-full py-2 bg-stone-100 hover:bg-stone-200 text-stone-800 text-xs font-bold rounded-xl transition">
              Load into Dressing Room
            </button>
          </div>

          <!-- Outfit 2 -->
          <div class="bg-white p-4 rounded-3xl border border-stone-200 shadow-sm flex flex-col justify-between">
            <div>
              <div class="h-44 bg-emerald-50/50 rounded-2xl flex items-center justify-center p-2 mb-3">
                <img src="{MODEL_EMERALD}" class="h-full object-contain">
              </div>
              <h4 class="font-bold text-sm text-stone-900">Zara Emerald Silk Wrap Maxi</h4>
              <p class="text-xs text-stone-500">Runway silk collection • High neck evening</p>
              <p class="text-sm font-extrabold text-stone-900 mt-1">$74.00 <span class="text-[10px] text-emerald-600 font-bold">(Coin voucher applied)</span></p>
            </div>
            <button onclick="navigateTo('view-studio'); selectOutfitLook('emerald');" class="mt-4 w-full py-2 bg-stone-100 hover:bg-stone-200 text-stone-800 text-xs font-bold rounded-xl transition">
              Load into Dressing Room
            </button>
          </div>

        </div>
      </div>

    </section>

  </main>

  <!-- CHECKOUT MODAL -->
  <div id="checkout-modal" class="fixed inset-0 bg-black/60 backdrop-blur-sm z-50 flex items-center justify-center p-4 hidden">
    <div class="bg-white max-w-md w-full rounded-[32px] p-6 shadow-2xl border border-stone-200 text-stone-800">
      <div class="flex items-center justify-between pb-3 border-b border-stone-100">
        <h3 class="font-serif font-bold text-lg text-stone-900">Doorstep Order Summary</h3>
        <button onclick="closeCheckoutModal()" class="w-7 h-7 rounded-full bg-stone-100 text-stone-500 hover:text-stone-800 font-bold text-sm">✕</button>
      </div>

      <div class="py-4 space-y-3">
        <div class="bg-stone-50 p-3.5 rounded-2xl border border-stone-200">
          <p class="text-xs font-bold text-stone-800 mb-1">Delivering to:</p>
          <p class="text-xs text-stone-600">Oreoluwa • Victoria Island, Lagos / London</p>
          <p class="text-[11px] text-emerald-700 font-semibold mt-1">✓ Estimated delivery: 2-3 business days</p>
        </div>

        <div class="flex justify-between items-center text-sm font-extrabold text-stone-900 py-1">
          <span>Amount Payable:</span>
          <span id="modal-total-val" class="text-lg text-stone-900">$543.89</span>
        </div>

        <div class="p-3 bg-amber-50 rounded-xl border border-amber-200 text-xs text-amber-900">
          🪙 <strong>150 Play Dress Up Coins redeemed!</strong> You earned +45 coins for this purchase.
        </div>
      </div>

      <div class="space-y-2">
        <button onclick="confirmOrder()" class="w-full py-3 bg-stone-900 hover:bg-black text-white rounded-2xl font-bold text-xs uppercase tracking-wider transition">
          Confirm & Pay Doorstep Delivery
        </button>
        <button onclick="closeCheckoutModal()" class="w-full py-2.5 bg-stone-100 hover:bg-stone-200 text-stone-700 rounded-2xl font-bold text-xs transition">
          Continue Styling
        </button>
      </div>
    </div>
  </div>

  <!-- JAVASCRIPT LOGIC -->
  <script>
    // Asset base64 URLs
    const ASSETS = {{
      model_minimalist: "{MODEL_HER_FASHION}",
      model_emerald: "{MODEL_EMERALD}",
      model_noir: "{MODEL_NOIR}",
      model_rose: "{MODEL_ROSE}",
      doll_2d: "{DOLL_2D}",
      prod_top: "{PROD_TOP}",
      prod_skirt: "{PROD_SKIRT}",
      prod_boots: "{PROD_BOOTS}",
      prod_bag: "{PROD_BAG}",
      prod_emerald: "{PROD_EMERALD}",
      prod_noir: "{PROD_NOIR}",
      prod_rose: "{PROD_ROSE}"
    }};

    // Navigation Router
    function navigateTo(viewId) {{
      document.querySelectorAll('.view-section').forEach(sec => {{
        sec.classList.remove('active');
      }});
      const target = document.getElementById(viewId);
      if (target) {{
        target.classList.add('active');
        window.scrollTo({{ top: 0, behavior: 'smooth' }});
      }}

      // Update Nav Button Active state
      document.querySelectorAll('.nav-btn').forEach(btn => {{
        if (btn.getAttribute('data-target') === viewId) {{
          btn.classList.add('active');
        }} else {{
          btn.classList.remove('active');
        }}
      }});
    }}

    // Avatar Engine Functions (Page 2)
    function updateMeasure(type, val) {{
      document.getElementById('val-' + type).innerText = val + ' in';
      document.getElementById('lbl-' + type).innerText = val + '"';
      showToast(`Updated ${{type}} to ${{val}} inches`, '📏');
    }}

    function setBodySilhouette(shape) {{
      document.getElementById('lbl-build').innerText = shape;
      document.querySelectorAll('.sil-btn').forEach(btn => {{
        btn.classList.remove('border-2', 'border-stone-900', 'bg-stone-50');
        btn.classList.add('border-stone-200');
      }});
      event.currentTarget.classList.add('border-2', 'border-stone-900', 'bg-stone-50');
      event.currentTarget.classList.remove('border-stone-200');
      showToast(`Silhouette set to ${{shape}}`, '⏳');
    }}

    function selectComplexion(name, hex) {{
      showToast(`Complexion selected: ${{name}}`, '✨');
    }}

    function saveAvatarAndGoStudio() {{
      showToast('Avatar dimensions saved!', '💾');
      setTimeout(() => {{
        navigateTo('view-studio');
      }}, 500);
    }}

    // Studio Avatar Mode Switcher: 3D Runway Model vs 2D Doll Avatar
    let avatarMode = '3d';
    function setAvatarMode(mode) {{
      avatarMode = mode;
      const modelImg = document.getElementById('center-model-img');
      const dollImg = document.getElementById('center-doll-img');
      const btn3d = document.getElementById('btn-mode-3d');
      const btn2d = document.getElementById('btn-mode-2d');

      if (mode === '3d') {{
        modelImg.style.display = 'block';
        dollImg.style.display = 'none';
        btn3d.className = 'px-3 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5 bg-stone-900 text-white shadow-sm';
        btn2d.className = 'px-3 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5 text-stone-600 hover:text-stone-900';
      }} else {{
        modelImg.style.display = 'none';
        dollImg.style.display = 'block';
        btn2d.className = 'px-3 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5 bg-stone-900 text-white shadow-sm';
        btn3d.className = 'px-3 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5 text-stone-600 hover:text-stone-900';
      }}
    }}

    // Curated Looks Logic
    let currentLook = 'minimalist';
    const itemState = {{ top: true, skirt: true, boots: true, bag: true }};
    const prices = {{ top: 29.90, skirt: 49.99, boots: 129.00, bag: 350.00 }};

    function selectOutfitLook(lookKey) {{
      currentLook = lookKey;
      const modelImg = document.getElementById('center-model-img');
      const tagText = document.getElementById('center-tag-text');
      const summaryText = document.getElementById('equipped-summary-text');
      const storeBrand = document.getElementById('store-brand-title');
      const lookBadge = document.getElementById('outfit-tag-badge');
      const itemsList = document.getElementById('your-look-items-list');

      document.querySelectorAll('.look-btn').forEach(btn => {{
        btn.classList.remove('bg-stone-900', 'text-white', 'border-stone-900');
        btn.classList.add('bg-stone-50', 'text-stone-800', 'border-stone-200');
      }});
      const activeBtn = document.getElementById('btn-look-' + lookKey);
      if (activeBtn) {{
        activeBtn.classList.add('bg-stone-900', 'text-white', 'border-stone-900');
        activeBtn.classList.remove('bg-stone-50', 'text-stone-800', 'border-stone-200');
      }}

      if (lookKey === 'minimalist') {{
        modelImg.src = ASSETS.model_minimalist;
        tagText.innerText = 'Look 1 • Neutral Luxe';
        summaryText.innerText = 'Wearing: Zara Top + Mango Skirt + Leather Boots + Coach Bag';
        storeBrand.innerText = 'HER FASHION';
        lookBadge.innerText = 'Curated 4-Piece Look';

        document.getElementById('fit-color-text').innerText = 'Color harmony: Warm Taupe & Cream';
        document.getElementById('fit-occasion-text').innerText = 'Occasion: Evening Casual / Art Gallery';

        itemsList.innerHTML = `
          <div id="row-top" class="flex items-center justify-between p-2.5 bg-stone-50 rounded-2xl border border-stone-200/80">
            <div class="flex items-center gap-2.5">
              <div class="w-9 h-9 rounded-xl bg-white border border-stone-200 flex items-center justify-center p-1 shadow-sm">
                <img src="${{ASSETS.prod_top}}" class="h-full object-contain">
              </div>
              <div>
                <span class="text-[9px] font-bold text-stone-400 uppercase">ZARA</span>
                <h4 class="text-xs font-bold text-stone-900 leading-tight">Off-shoulder top</h4>
                <p class="text-xs font-extrabold text-stone-900 mt-0.5">$29.90</p>
              </div>
            </div>
            <span class="text-stone-400 text-xs font-bold">›</span>
          </div>
          <div id="row-skirt" class="flex items-center justify-between p-2.5 bg-stone-50 rounded-2xl border border-stone-200/80">
            <div class="flex items-center gap-2.5">
              <div class="w-9 h-9 rounded-xl bg-white border border-stone-200 flex items-center justify-center p-1 shadow-sm">
                <img src="${{ASSETS.prod_skirt}}" class="h-full object-contain">
              </div>
              <div>
                <span class="text-[9px] font-bold text-stone-400 uppercase">MANGO</span>
                <h4 class="text-xs font-bold text-stone-900 leading-tight">Pleated maxi skirt</h4>
                <p class="text-xs font-extrabold text-stone-900 mt-0.5">$49.99</p>
              </div>
            </div>
            <span class="text-stone-400 text-xs font-bold">›</span>
          </div>
          <div id="row-boots" class="flex items-center justify-between p-2.5 bg-stone-50 rounded-2xl border border-stone-200/80">
            <div class="flex items-center gap-2.5">
              <div class="w-9 h-9 rounded-xl bg-white border border-stone-200 flex items-center justify-center p-1 shadow-sm">
                <img src="${{ASSETS.prod_boots}}" class="h-full object-contain">
              </div>
              <div>
                <span class="text-[9px] font-bold text-stone-400 uppercase">BERSHKA</span>
                <h4 class="text-xs font-bold text-stone-900 leading-tight">Leather boots</h4>
                <p class="text-xs font-extrabold text-stone-900 mt-0.5">$129.00</p>
              </div>
            </div>
            <span class="text-stone-400 text-xs font-bold">›</span>
          </div>
          <div id="row-bag" class="flex items-center justify-between p-2.5 bg-stone-50 rounded-2xl border border-stone-200/80">
            <div class="flex items-center gap-2.5">
              <div class="w-9 h-9 rounded-xl bg-white border border-stone-200 flex items-center justify-center p-1 shadow-sm">
                <img src="${{ASSETS.prod_bag}}" class="h-full object-contain">
              </div>
              <div>
                <span class="text-[9px] font-bold text-stone-400 uppercase">COACH</span>
                <h4 class="text-xs font-bold text-stone-900 leading-tight">Tabby shoulder bag</h4>
                <p class="text-xs font-extrabold text-stone-900 mt-0.5">$350.00</p>
              </div>
            </div>
            <span class="text-stone-400 text-xs font-bold">›</span>
          </div>
        `;

        updateTotals(558.89);
        updateCardBadges('minimalist');

      }} else if (lookKey === 'emerald') {{
        modelImg.src = ASSETS.model_emerald;
        tagText.innerText = 'Look 2 • Emerald Silk Maxi';
        summaryText.innerText = 'Wearing: Zara Emerald Silk Wrap Maxi Dress';
        storeBrand.innerText = 'ZARA FLAGSHIP';
        lookBadge.innerText = 'Runway Silk Collection';

        document.getElementById('fit-color-text').innerText = 'Color harmony: Deep Jewel Emerald Green';
        document.getElementById('fit-occasion-text').innerText = 'Occasion: Gala / Cocktail Soirée';

        itemsList.innerHTML = `
          <div class="flex items-center justify-between p-2.5 bg-emerald-50/70 rounded-2xl border border-emerald-200">
            <div class="flex items-center gap-2.5">
              <div class="w-9 h-9 rounded-xl bg-white border border-emerald-200 flex items-center justify-center p-1 shadow-sm">
                <img src="${{ASSETS.prod_emerald}}" class="h-full object-contain">
              </div>
              <div>
                <span class="text-[9px] font-bold text-emerald-700 uppercase">ZARA</span>
                <h4 class="text-xs font-bold text-stone-900 leading-tight">Emerald silk wrap maxi</h4>
                <p class="text-xs font-extrabold text-stone-900 mt-0.5">$89.00</p>
              </div>
            </div>
            <span class="text-emerald-600 text-xs font-bold">✓</span>
          </div>
        `;

        updateTotals(89.00);
        updateCardBadges('emerald');

      }} else if (lookKey === 'noir') {{
        modelImg.src = ASSETS.model_noir;
        tagText.innerText = 'Look 3 • Noir Velvet';
        summaryText.innerText = 'Wearing: Mango Noir Velvet Slip Gown';
        storeBrand.innerText = 'MANGO STUDIO';
        lookBadge.innerText = 'Evening Capsule';

        document.getElementById('fit-color-text').innerText = 'Color harmony: Midnight Black Velvet';
        document.getElementById('fit-occasion-text').innerText = 'Occasion: Black Tie Event';

        itemsList.innerHTML = `
          <div class="flex items-center justify-between p-2.5 bg-stone-100 rounded-2xl border border-stone-200">
            <div class="flex items-center gap-2.5">
              <div class="w-9 h-9 rounded-xl bg-white border border-stone-200 flex items-center justify-center p-1 shadow-sm">
                <img src="${{ASSETS.prod_noir}}" class="h-full object-contain">
              </div>
              <div>
                <span class="text-[9px] font-bold text-stone-500 uppercase">MANGO</span>
                <h4 class="text-xs font-bold text-stone-900 leading-tight">Noir velvet slip gown</h4>
                <p class="text-xs font-extrabold text-stone-900 mt-0.5">$119.00</p>
              </div>
            </div>
            <span class="text-stone-800 text-xs font-bold">✓</span>
          </div>
        `;

        updateTotals(119.00);
        updateCardBadges('noir');

      }} else if (lookKey === 'rose') {{
        modelImg.src = ASSETS.model_rose;
        tagText.innerText = 'Look 4 • Rose Quartz';
        summaryText.innerText = 'Wearing: Rose Quartz Satin Wrap Dress';
        storeBrand.innerText = 'H&M PREMIUM';
        lookBadge.innerText = 'Summer Soirée';

        document.getElementById('fit-color-text').innerText = 'Color harmony: Blush Pink & Pearl';
        document.getElementById('fit-occasion-text').innerText = 'Occasion: Afternoon Tea / Date Night';

        itemsList.innerHTML = `
          <div class="flex items-center justify-between p-2.5 bg-rose-50 rounded-2xl border border-rose-200">
            <div class="flex items-center gap-2.5">
              <div class="w-9 h-9 rounded-xl bg-white border border-rose-200 flex items-center justify-center p-1 shadow-sm">
                <img src="${{ASSETS.prod_rose}}" class="h-full object-contain">
              </div>
              <div>
                <span class="text-[9px] font-bold text-rose-500 uppercase">H&M</span>
                <h4 class="text-xs font-bold text-stone-900 leading-tight">Rose quartz satin dress</h4>
                <p class="text-xs font-extrabold text-stone-900 mt-0.5">$79.00</p>
              </div>
            </div>
            <span class="text-rose-500 text-xs font-bold">✓</span>
          </div>
        `;

        updateTotals(79.00);
        updateCardBadges('rose');
      }}
    }}

    function updateCardBadges(lookKey) {{
      const cards = ['top', 'skirt', 'boots', 'bag', 'emerald', 'noir'];
      cards.forEach(k => {{
        const card = document.getElementById('card-' + k);
        const badge = document.getElementById('badge-' + k);
        if (card && badge) {{
          if (lookKey === 'minimalist' && ['top', 'skirt', 'boots', 'bag'].includes(k)) {{
            card.classList.add('card-active-equipped');
            badge.innerText = 'Equipped ✓';
            badge.className = 'text-[9px] bg-stone-900 text-white font-bold px-1.5 py-0.5 rounded';
          }} else if (k === lookKey) {{
            card.classList.add('card-active-equipped');
            badge.innerText = 'Equipped ✓';
            badge.className = 'text-[9px] bg-stone-900 text-white font-bold px-1.5 py-0.5 rounded';
          }} else {{
            card.classList.remove('card-active-equipped');
            badge.innerText = 'Tap to Add';
            badge.className = 'text-[9px] bg-stone-100 text-stone-500 font-bold px-1.5 py-0.5 rounded';
          }}
        }}
      }});
    }}

    function toggleSingleItem(key) {{
      if (currentLook !== 'minimalist') {{
        selectOutfitLook('minimalist');
        return;
      }}

      itemState[key] = !itemState[key];
      const isEquipped = itemState[key];

      const card = document.getElementById('card-' + key);
      const badge = document.getElementById('badge-' + key);
      const row = document.getElementById('row-' + key);
      const mini = document.getElementById('mini-' + key);

      if (card) {{
        if (isEquipped) card.classList.add('card-active-equipped');
        else card.classList.remove('card-active-equipped');
      }}
      if (badge) {{
        badge.innerText = isEquipped ? 'Equipped ✓' : 'Tap to Add';
        badge.className = isEquipped 
          ? 'text-[9px] bg-stone-900 text-white font-bold px-1.5 py-0.5 rounded'
          : 'text-[9px] bg-stone-100 text-stone-500 font-bold px-1.5 py-0.5 rounded';
      }}
      if (row) row.style.opacity = isEquipped ? '1' : '0.3';
      if (mini) mini.style.opacity = isEquipped ? '1' : '0.2';

      let sub = 0;
      const equipped = [];
      if (itemState.top) {{ sub += prices.top; equipped.push('Zara Top'); }}
      if (itemState.skirt) {{ sub += prices.skirt; equipped.push('Mango Skirt'); }}
      if (itemState.boots) {{ sub += prices.boots; equipped.push('Leather Boots'); }}
      if (itemState.bag) {{ sub += prices.bag; equipped.push('Coach Bag'); }}

      document.getElementById('equipped-summary-text').innerText = equipped.length > 0
        ? 'Wearing: ' + equipped.join(' + ')
        : 'Avatar in underlayer • Tap items to dress up';

      updateTotals(sub);
    }}

    function updateTotals(subtotal) {{
      const subtotalEl = document.getElementById('subtotal-val');
      const totalEl = document.getElementById('total-val');
      const modalTotal = document.getElementById('modal-total-val');

      const discount = subtotal > 15 ? 15.00 : 0;
      const total = Math.max(0, subtotal - discount);

      subtotalEl.innerText = '$' + subtotal.toFixed(2);
      totalEl.innerText = '$' + total.toFixed(2);
      if (modalTotal) modalTotal.innerText = '$' + total.toFixed(2);
    }}

    function filterCategory(cat) {{
      document.querySelectorAll('.cat-pill').forEach(btn => {{
        btn.classList.remove('bg-stone-900', 'text-white');
        btn.classList.add('bg-stone-100', 'text-stone-700');
      }});
      event.target.classList.add('bg-stone-900', 'text-white');
      event.target.classList.remove('bg-stone-100', 'text-stone-700');
      showToast(`Filtered category: ${{cat}}`, '🔍');
    }}

    function toggleFav(btn) {{
      btn.classList.toggle('text-red-500');
      btn.innerText = btn.classList.contains('text-red-500') ? '♥' : '♡';
      showToast('Item saved to wishlist!', '💖');
    }}

    function openCheckoutModal() {{
      document.getElementById('checkout-modal').classList.remove('hidden');
    }}

    function closeCheckoutModal() {{
      document.getElementById('checkout-modal').classList.add('hidden');
    }}

    function confirmOrder() {{
      alert('🎉 Order Placed Successfully! Your curated outfit has been confirmed for doorstep delivery. 150 Coins applied as discount!');
      closeCheckoutModal();
    }}

    function startChallenge(look) {{
      navigateTo('view-studio');
      selectOutfitLook(look);
      showToast(`Challenge theme loaded into dressing room!`, '🏆');
    }}

    function saveCurrentLookToWardrobe() {{
      showToast('🎉 Outfit look saved to your Wardrobe!', '💾');
      const countEl = document.getElementById('nav-saved-count');
      if (countEl) countEl.innerText = parseInt(countEl.innerText) + 1;
    }}

    function showToast(msg, icon = '✨') {{
      const toast = document.getElementById('app-toast');
      document.getElementById('toast-msg').innerText = msg;
      document.getElementById('toast-icon').innerText = icon;
      toast.classList.remove('translate-y-24', 'opacity-0');
      setTimeout(() => {{
        toast.classList.add('translate-y-24', 'opacity-0');
      }}, 3000);
    }}
  </script>
</body>
</html>
"""

# Write out to all targets
target_index = '/home/gamp/.gemini/antigravity/scratch/play-dress-up-web/index.html'
target_blueprint = '/home/gamp/.gemini/antigravity/scratch/play-dress-up-web/blueprint.html'
artifact_path = '/home/gamp/.gemini/antigravity/brain/5988c679-a518-4b3a-a908-6a809de30903/visual_design_blueprints.html'

for path in [target_index, target_blueprint, artifact_path]:
    with open(path, 'w') as f:
        f.write(html_code)

print("Complete Play Dress Up platform built with all pages!")
