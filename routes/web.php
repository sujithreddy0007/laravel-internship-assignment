<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\Caller\LoginController;
use App\Http\Controllers\EventController;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
*/

// Login Routes
Route::get('/', [LoginController::class, 'index']);
Route::get('/login', [LoginController::class, 'index'])->name('login');
Route::post('/login', [LoginController::class, 'validateUser']);
Route::get('/login/{driver}/start', [LoginController::class, 'redirectToProvider']);
Route::any('/login/{driver}/callback', [LoginController::class, 'handleProviderCallback']);
Route::any('/logout', [LoginController::class, 'Logout']);


// Calendar Page
Route::get('/calendar', function () {
    return view('calendar');
})->name('calendar');


// Calendar API Routes
Route::get('/events', [EventController::class, 'index']);
Route::post('/events', [EventController::class, 'store']);
