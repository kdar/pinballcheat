/////////////////////////////////////////////////////////////////////////////
// Name:        
// Purpose:     
// Author:      
// Modified by: 
// Created:     07/03/2007 18:49:06
// RCS-ID:      
// Copyright:   
// Licence:     
/////////////////////////////////////////////////////////////////////////////

#ifndef _APP_RESOURCES_H_
#define _APP_RESOURCES_H_

#if defined(__GNUG__) && !defined(NO_GCC_PRAGMA)
#pragma interface ""
#endif

/*!
 * Control identifiers
 */

////@begin control identifiers
#define Id_HighScore_Shiftup_Cmd 10022
#define Id_HighScore_Shiftdown_Cmd 10023
#define Id_HighScore_Reset_Cmd 10020
#define Id_HighScore_SaveToFile_Cmd 10030
#define Id_HighScore_LoadFromFile_Cmd 10031
////@end control identifiers

class AppResources
{
public:
    AppResources() {}

/*!
 * Resource functions
 */

////@begin AppResources resource functions
    /// Menu creation function for Id_HighScore_Menu
    static wxMenu* CreateMenuMenu();

    /// Retrieves bitmap resources
    static wxBitmap GetBitmapResource( const wxString& name );

    /// Retrieves icon resources
    static wxIcon GetIconResource( const wxString& name );
////@end AppResources resource functions

};

#endif
    // _APP_RESOURCES_H_
