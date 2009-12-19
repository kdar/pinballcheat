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

#if defined(__GNUG__) && !defined(NO_GCC_PRAGMA)
#pragma implementation ""
#endif

// For compilers that support precompilation, includes "wx/wx.h".
#include "wx/wxprec.h"

#ifdef __BORLANDC__
#pragma hdrstop
#endif

#ifndef WX_PRECOMP
#include "wx/wx.h"
#endif

////@begin includes
////@end includes

#include "app_resources.h"

////@begin XPM images
////@end XPM images

/*!
 * Resource functions
 */

////@begin AppResources resource functions
/*!
 * Menu creation function for Id_HighScore_Menu
 */

wxMenu* AppResources::CreateMenuMenu()
{
    wxMenu* itemMenu1 = new wxMenu;
    itemMenu1->Append(Id_HighScore_Shiftup_Cmd, _("Shift up"), _T(""), wxITEM_NORMAL);
    itemMenu1->Append(Id_HighScore_Shiftdown_Cmd, _("Shift down"), _T(""), wxITEM_NORMAL);
    itemMenu1->AppendSeparator();
    itemMenu1->Append(Id_HighScore_Reset_Cmd, _("Reset"), _T(""), wxITEM_NORMAL);
    itemMenu1->AppendSeparator();
    itemMenu1->Append(Id_HighScore_SaveToFile_Cmd, _("Save to file"), _T(""), wxITEM_NORMAL);
    itemMenu1->Append(Id_HighScore_LoadFromFile_Cmd, _("Load from file"), _T(""), wxITEM_NORMAL);
    return itemMenu1;
}

////@end AppResources resource functions

/*!
 * Get bitmap resources
 */

wxBitmap AppResources::GetBitmapResource( const wxString& name )
{
    // Bitmap retrieval
////@begin AppResources bitmap retrieval
    wxUnusedVar(name);
    return wxNullBitmap;
////@end AppResources bitmap retrieval
}

/*!
 * Get icon resources
 */

wxIcon AppResources::GetIconResource( const wxString& name )
{
    wxUnusedVar(name);
    // Icon retrieval
////@begin AppResources icon retrieval
    wxUnusedVar(name);
    return wxNullIcon;
////@end AppResources icon retrieval
}
